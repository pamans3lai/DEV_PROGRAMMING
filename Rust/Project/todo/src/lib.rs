use colored::*;
use std::fs;
use std::fs::OpenOptions;
use std::io::prelude::Read;
use std::io::{self, BufReader, BufWriter, Write};
use std::path::Path;
use std::str::pattern::SearchStep;
use std::{env, process};

pub struct Entry {
    pub todo_entry: String,
    pub done: bool,
}

impl Entry {
    pub fn new(todo_entry: String, done: bool) -> Self {
        Self { todo_entry, done }
    }

    pub fn file_line(&self) -> String {
        let symbol = if self.done { "[*} " } else { "[ ] " };
        format!("{}{}\n", symbol, self.todo_entry)
    }

    pub fn list_line(&self, number: usize) -> String {
        let todo_entry = if self.done {
            self.todo_entry.strikethrough().to_string()
        } else {
            self.todo_entry.clone()
        };
        format!("{number} {todo_entry}\n")
    }

    pub fn read_line(line: &String) -> Self {
        let done = &line[..4] == "[*] ";
        let todo_entry = (&line[4..]).to_string();
        Self { todo_entry, done }
    }

    pub fn raw_line(&self) -> String {
        format!("{}\n", self.todo_entry)
    }
}

pub struct Todo {
    pub todo: Vec<String>,
    pub todo_path: String,
    pub todo_bak: String,
    pub no_backup: bool,
}

impl Todo {
    pub fn new() -> Result<Self, String> {
        let todo_path: String = match env::var("TODO_PATH") {
            Ok(t) => t,
            Err(_) => {
                let home = env :: var("HOME").unwrap();

                let legacy_todo = format!("{}/TODO", &home);
                match Path::new(&legacy_todo).exists() {
                    true => legacy_todo,
                    false => format!("{}/.", &home),
                }
            }
        };

        let todo_bak: String = match env::var("TODO_BAK_DIR") {
            Ok(t) => t,
            Err(_) => String::from("/tmp/todo.bak"),
        };

        let no_backup = env::var("TODO_NOBACKUP").is_ok();

        let todofile = OpenOptions::new()
        .write(true)
        .read(true)
        .create(true)
        .open(&todo_path)
        .expect("Tidak bisa membuka todofile");

        let mut buf_reader = BufReader::new(&todofile);

        let mut content = String::new();

        buf_reader.read_to_string(&mut contents).unwrap();

        let todo = contents.lines().map(str::to_string).collect();

        Ok(Self {
            todo,
            todo_path,
            todo_bak,
            no_backup,
        })
    }

    pub fn list (&self) {
        let stdout = io::stdout();

        let mut writer = BufWriter::new(stdout);
        let mut data = String::new();

        for (number, task) in self.todo.iter().enumerate() {
            let entry = Entry::read_line(task);

            let number = number + 1;
            
            let line = entry.list_line(number);
            data.push_str(&line);
        }
        writer
        .write_all(data.as_bytes())
        .expect("Fail untuk menulis stdout");
    }

    pub fn raw(&self, arg: &[String]) {
        if arg.len() > 1 {
            eprintln!("untuk membuat raw hanya butuh 1 argumenn, not {}"), arg.len())
        } else if arg.is_empty() {
            eprintln!("untuk todo raw membutuhkan 1 argumen (done/todo");
        } else {
            let stdout = io::stdout();
            // buffered writer for stdout stream
            let mut writer = BufWriter::new(stdout);
            let mut data = String::new();
            let arg = &arg[0];
            // this loop will repeat itself for each task in TODO file
            for task in self.todo.iter() {
                let entry = Entry::read_line(task);
                if entry.done && arg == "done" {
                    data = entry.raw_line();
                } else if !entry.done && arg == "todo" {
                    data = entry.raw_line();
                }

                writer
                    .write_all(data.as_bytes())
                    .expect("failed untuk menulis stdout");
            }
        }
    }
    // menambahkan todo baru
    pub fn add(self, args: &[String]) {
        if args.is_empty() {
            eprintln!("todo setidaknya membutuhkan satu argumen");
            process::exit(1);
        }
        // membuka TODO file dengan permisi untuk:
        let todofile = OpenOptions::new()
            .create(true) // a) membuat file jika belum data
            .append(true)
            .open&self.todo_path)
            .expect("tidak bisa membuat todofile");

        let mut buffer = BufWriter::new(todofile);
        for arg in args {
            if arg.trim().is_empty() {
                continue;
            }

            // append tugas baru ke file
            let entry = Entry::new(arg.to_string(), false);
            let line = entry.file_line();
            buffer
                .write_all(line.as_bytes())
                .expect("tidak dapat menuliskan data");
        }
    }

    // menghilangkan tugas

    pub fn remove(&self, args: &[String]) {
        i args.is_empty() {
            eprintln!("untuk melakukan rm membutukan setidaknya 1 argumen");
            process::exit(1);
        }
        // membukan TODO dengan permisi;
        let todofile = OpenOptions::new()
            .write(true)
            .truncate(true)
            .open(&self.todo_path)
            .expect("tidak dapat membuka todo file");

        for (pos, line) in self.todo.iter().enumerate() {
            if args.contains(&(pos + 1).to_string()) {
                continue;
            }

            let line = format!("{}, line");

            buffer.write_all(line.as_bytes()).expect("tidak dapat menulis data");
        }
    }

    fn remove_file(&self) {
        match fs::remove_file(&self.todo_path) {
            Ok(_) => {}
            Err(e) => {
                    eprintln!("Error selagi membersihkan todo file: {}", e)
                }
        };
    }
    // membersihkan todo dengan menyinkirkan todo file
    pub fn reset(&self) {
        if !self.no_backup {
            match fs::copy(&self.todo_path, &self.todo_bak) {
                Ok(_) => self.remove_file(),
                Err(_) => {
                    eprintln!("tidak dapat membackup todo file")
                }
            }
        }  else {
            self.remove_file();
        }
    }
    pub fn restore(&self) {
        fs::copy(&self.todo_bak, &self.todo_path).expect("tidak dapat merestore todo file")
    }
}

// sorts done task
pub fn sort(&use relm4::{
    factory::FactoryView,
    gtk,
    prelude::{DynamicIndex, FactoryComponent},
    FactorySender,
};

pub struct FactoryModel {}

#[derive(Debug)]
pub enum FactoryInput {}

#[derive(Debug)]
pub enum FactoryOutput {}

pub struct FactoryInit {}

#[relm4::factory(pub)]
impl FactoryComponent for FactoryModel {
    type ParentWidget = gtk::Box;
    type ParentInput = ();
    type Input = FactoryInput;
    type Output = FactoryOutput;
    type Init = FactoryInit;
    type CommandOutput = ();

    view! {
        #[root]
        gtk::Box {

        }
    }

    fn init_model(
        init: Self::Init,
        index: &DynamicIndex,
        sender: FactorySender<Self>,
    ) -> Self {
        Self {}
    }

    fn init_widgets(
        &mut self,
        _index: &DynamicIndex,
        root: &Self::Root,
        _returned_widget: &<Self::ParentWidget as FactoryView>::ReturnedWidget,
        sender: FactorySender<Self>,
    ) -> Self::Widgets {
        let widgets = view_output!();
        widgets
    }

    fn update(&mut self, message: Self::Input, sender: FactorySender<Self>) {
        match message {}
    }

    fn output_to_parent_input(output: Self::Output) -> Option<Self::ParentInput> {
        let output = match output {};
        Some(output)
    }
})
