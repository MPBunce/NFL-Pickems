package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"net/http"
	"os"
	"time"

	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

const version = "1.0.0"

type config struct {
	port int
	env  string
	db   string
}

type application struct {
	config   config
	logger   *log.Logger
	dbClient *mongo.Client
}

func main() {

	var cfg config

	flag.IntVar(&cfg.port, "port", 4000, "API server port")
	flag.StringVar(&cfg.env, "env", "development", "Environment (development|staging|production)")
	flag.StringVar(&cfg.db, "db", "", "mongoDB")
	flag.Parse()

	logger := log.New(os.Stdout, "", log.Ldate|log.Ltime)

	mongoClient, b := openDB(cfg)
	if b != nil {
		fmt.Printf("Error with database \n")
		fmt.Println(b)
	}
	defer func() {
		if b = mongoClient.Disconnect(context.TODO()); b != nil {
			panic(b)
		}
	}()

	app := &application{
		config:   cfg,
		logger:   logger,
		dbClient: mongoClient,
	}

	srv := &http.Server{
		Addr:         fmt.Sprintf(":%d", cfg.port),
		Handler:      app.routes(),
		IdleTimeout:  time.Minute,
		ReadTimeout:  10 * time.Second,
		WriteTimeout: 30 * time.Second,
	}

	logger.Printf("starting %s server on %s", cfg.env, srv.Addr)

	err := srv.ListenAndServe()
	logger.Fatal(err)

}

func openDB(cfg config) (*mongo.Client, error) {

	clientOptions := options.Client().ApplyURI(cfg.db)
	client, err := mongo.Connect(context.Background(), clientOptions)
	if err != nil {
		return nil, err
	}
	return client, nil

}
