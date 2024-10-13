package main

import (
	"net/http"

	"github.com/julienschmidt/httprouter"
)

func (app *application) routes() *httprouter.Router {

	router := httprouter.New()

	//Health Check Routes
	router.HandlerFunc(http.MethodGet, "/", app.healthcheckHandler)

	//Picks And Standings Routes
	router.HandlerFunc(http.MethodPost, "/v1/login", app.createMovieHandler)
	router.HandlerFunc(http.MethodPost, "/v1/register", app.createMovieHandler)

	//Picks And Standings Routes
	router.HandlerFunc(http.MethodPost, "/v1/lockin_picks", app.createMovieHandler)
	router.HandlerFunc(http.MethodGet, "/v1/get_picks", app.showMovieHandler)

	router.HandlerFunc(http.MethodGet, "/v1/picks_standings", app.showMovieHandler)
	router.HandlerFunc(http.MethodGet, "/v1/picks_standings/season", app.showMovieHandler)

	router.HandlerFunc(http.MethodGet, "/v1/nfl_standings", app.showMovieHandler)
	router.HandlerFunc(http.MethodGet, "/v1/nfl_standings/season", app.showMovieHandler)

	return router
}
