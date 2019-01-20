package digitalocean

import (
	"encoding/json"
	"flag"
	"fmt"
	"io/ioutil"
)

type config struct {
	APIToken string `json:"api_token"`
	Project  string `json:"project"`
}

var defaultConfig = &config{
	APIToken: "",
	Project:  "",
}

func Run() error {
	dat, err := ioutil.ReadFile("digitalocean.conf")
	if err == nil {
		err = json.Unmarshal(dat, defaultConfig)
		if err != nil {
			return err
		}

	}
	flagToken := flag.String("token", defaultConfig.APIToken, "Auth token for DigitalOcean")
	flagProject := flag.String("project", defaultConfig.Project, "DigitalOcean project")

	conf := &config{
		APIToken: *flagToken,
		Project:  *flagProject,
	}
	fmt.Println(*conf)
}

//Interface
type DigitalOcean struct{}

func (d *DigitalOcean) RunCLI(args []string) error {
	return Run()
}
