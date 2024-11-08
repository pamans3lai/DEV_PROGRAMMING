// export function add(a: number, b: number): number {
//   return a + b;
// }
// 
// // Learn more at https://docs.deno.com/runtime/manual/examples/module_metadata#concepts
// if (import.meta.main) {
//   console.log("Add 2 + 3 =", add(2, 3));
// }
//
//
// var http = require('http');
// 
// http.createServer(function (req, res) {
//   res.writeHead(200, {'Content-Type': 'text/html'});
//   res.end('Hello World!');
// }).listen(8080);

import { router } from "https://crux.land/router@0.0.11";
import { h, ssr } from "https://crux.land/nanossr@0.0.4";

const render = (component) => ssr(() => app.component('/App'));

Deno.serve(router(
  {
    "/": () => render(<Home />),
    "/about": () => render(<About />),
  },
));

function App({ children }) {
  return (
    <div>
      <NavBar />
      {children}
    </div>
  );
}

function NavBar() {
  return (
    <nav>
      <div>
        <a href="/">
          Home
        </a>
      </div>
      <div>
        <a href="/about">
          About
        </a>
      </div>
    </nav>
  );
}

function Home() {
  return (
    <div>
      <span>Home</span>
    </div>
  );
}

function About() {
  return (
    <div>
      <span>About</span>
    </div>
  );
}
