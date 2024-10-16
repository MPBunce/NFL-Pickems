package main

import (
	"net/http"

	"github.com/julienschmidt/httprouter"
)

func (app *application) routes() *httprouter.Router {

	router := httprouter.New()

	//Health Check Routes
	router.HandlerFunc(http.MethodGet, "/", app.healthcheckHandler)

	//Season Routes
	router.GET("/v1/seasons", app.allSeasonStandings)
	router.GET("/v1/seasons/:year", app.seasonStandings)

	//Picks And Standings Routes

	return router
}
