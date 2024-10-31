package main

import (
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/julienschmidt/httprouter"
	"google.golang.org/api/idtoken"
)

func (app *application) getUser(w http.ResponseWriter, r *http.Request, _ httprouter.Params) {

	payload, err := idtoken.ParsePayload(tokenString)
	if err != nil {
		panic(err)
	}
	fmt.Print(payload.Claims)
	json.NewEncoder(w).Encode(payload.Claims)

}
