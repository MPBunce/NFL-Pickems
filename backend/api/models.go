package main

import (
	"go.mongodb.org/mongo-driver/bson/primitive"
)

type SeasonStandings struct {
	ID    primitive.ObjectID `bson:"_id,omitempty"`
	Year  string             `bson:"year"`
	Teams []TeamData         `bson:"teams"`
}

type TeamData struct {
	Team         string `bson:"team"`
	Wins         int    `bson:"wins"`
	Losses       int    `bson:"losses"`
	Ties         int    `bson:"ties"`
	Division     string `bson:"division"`
	DivisionRank int    `bson:"division_rank"`
	Year         string `bson:"year"`
}
