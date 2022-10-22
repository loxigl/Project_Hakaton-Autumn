package main

import (
	"./index"
	"./login"
	"./reg"
	"net/http"
)

func handleFunc() {
	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("./static"))))
	http.HandleFunc("/", index.Index)
	http.HandleFunc("/login", login.Login)
	http.HandleFunc("/userlogin", login.Userlogin)
	http.HandleFunc("/registration", reg.RegPage)
	http.ListenAndServe(":8080", nil)
}

func main() {
	handleFunc()
}