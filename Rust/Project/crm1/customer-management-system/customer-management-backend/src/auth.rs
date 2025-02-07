use actix_web::{web, App, HttpRequest, HttpResponse, HttpServer};
use outh2_server::{AuthorizationCode, ClientCredentials};

#[actix_web::main]

async fn main() -> std::io::Result<()> {
    // ...
    //
    HttpServer::new(move || {
        App::new()
        .service(web::resource("/login").route(web::post()
            to(login)
        ))
    })
        .bind("127.0.0.8080")?
    .run()
            .await
}

async fn login(req: HttpRequest) -> HttpResponse {
    let username = req.match_info().get("username").unwrap();
    let password = req.match_info().get("password").unwrap();

    // Authenticate the username
    if username == "john" && password == "password" {
        let token = jwt::encode("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9", &["user_id", "username", "email"])
            .unwrap();
        HttpResponse::Ok().json(token)
    } else {
        HttpResponse::Unauthorized().body("Invalid credentials")
    }
}

async fn protected(req: HttpRequest) -> HttpResponse {
    let token = req.app_data::<String>().unwrap();

    // Verify the token and return a HttpResponse
    HttpResponse::Ok().body("Hello, world!")
}
