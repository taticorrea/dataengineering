package main

import (
	"encoding/json"
	"fmt"
	"os"
	"os/exec"
)

type JsonFileStruct struct {
	Tables []struct {
		Type   string `json:"type"`
		Target struct {
			Schema   string `json:"schema"`
			Name     string `json:"name"`
			Database string `json:"database"`
		} `json:"target"`
		Query            string `json:"query"`
		Disabled         bool   `json:"disabled"`
		FileName         string `json:"fileName"`
		ActionDescriptor struct {
			Columns []struct {
				Description string   `json:"description"`
				Path        []string `json:"path"`
			} `json:"columns"`
		} `json:"actionDescriptor"`
		CanonicalTarget struct {
			Schema   string `json:"schema"`
			Name     string `json:"name"`
			Database string `json:"database"`
		} `json:"canonicalTarget"`
	} `json:"tables"`
	ProjectConfig struct {
		Warehouse       string `json:"warehouse"`
		DefaultSchema   string `json:"defaultSchema"`
		AssertionSchema string `json:"assertionSchema"`
		DefaultDatabase string `json:"defaultDatabase"`
		DefaultLocation string `json:"defaultLocation"`
	} `json:"projectConfig"`
	GraphErrors struct {
	} `json:"graphErrors"`
	DataformCoreVersion string `json:"dataformCoreVersion"`
	Targets             []struct {
		Schema   string `json:"schema"`
		Name     string `json:"name"`
		Database string `json:"database"`
	} `json:"targets"`
}

func runDataformCompile() []byte {

	cmd := "dataform"
	args1 := "compile"
	args2 := "--json"

	jsonFile, err := exec.Command(cmd, args1, args2).Output()

	if err != nil {
		fmt.Println(err)
	}
	return jsonFile
}

func getSqlStatment() {

	jsonFile := runDataformCompile()

	objjson := JsonFileStruct{}
	json.Unmarshal(jsonFile, &objjson)

	os.MkdirAll("compiled_sql_go/", 0755)

	for i, tables := range objjson.Tables {
		query, err := os.OpenFile(fmt.Sprintf("compiled_sql_go/%s.sql", tables.Target.Name), os.O_RDWR|os.O_CREATE, 0777)

		if err != nil {
			fmt.Println(err, i)
		}

		query.WriteString(tables.Query)
	}
}

func main() {

	getSqlStatment()

}
