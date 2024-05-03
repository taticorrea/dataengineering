package main

import (
	"bufio"
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"
)

const monitoramentos = 4
const delay = 1

func exibirIntroducao() {
	nome := "Tatiane"
	versao := 1.0
	fmt.Println("Olá sra.", nome)
	fmt.Println("Este programa está na versão", versao)
}

func lerComando() int {
	var cmd int
	fmt.Scan(&cmd)
	fmt.Println("O comando escolhido foi ", cmd)

	return cmd
}

func exibirMenu() {
	fmt.Println("1 - Iniciar Monitoramento")
	fmt.Println("2 - Exibir Logs")
	fmt.Println("0 - Sair do programa")
}

func iniciarMonitoramento() {
	fmt.Println("Monitorando ...")
	urls := lerArquivosDeSites()

	for i := 0; i < monitoramentos; i++ {
		// for i := 0; i < len(urls); i++ {}
		for i, url := range urls {
			fmt.Println("Testando site", i, ":", url)
			testarSite(url)

		}

		time.Sleep(delay * time.Second)
		fmt.Println("")

	}

}

func testarSite(url string) {
	resp, err := http.Get(url)

	if err != nil {
		fmt.Println("Ocorreu um erro", err)

	}

	if resp.StatusCode == 200 {
		fmt.Println("O site", url, "foi carregado com sucesso")
		registrarLog(url, true)
	} else {
		fmt.Println("O site", url, "está com problemas. Status Code: ", resp.StatusCode)
		registrarLog(url, false)
	}
}

func lerArquivosDeSites() []string {
	var urls []string
	arquivo, err := os.Open("urls.txt")

	if err != nil {
		fmt.Println("Ocorreu um erro", err)
	}

	leitor := bufio.NewReader(arquivo)
	for {
		linha, err := leitor.ReadString('\n')
		linha = strings.TrimSpace(linha)

		urls = append(urls, linha)

		if err == io.EOF {
			break
		}
	}

	arquivo.Close()
	return urls

}

func registrarLog(url string, status bool) {

	arquivo, err := os.OpenFile("log.txt", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)

	if err != nil {
		fmt.Println("Ocorreu um erro", err)
	}

	arquivo.WriteString(time.Now().Format("02/01/2006 15:04:05 - ") + url + "- online: " + strconv.FormatBool(status) + "\n")

	arquivo.Close()
}

func imprimirLog() {
	arquivo, err := ioutil.ReadFile("log.txt")

	if err != nil {
		fmt.Println("Um erro ocorreu", err)
	}

	fmt.Println(string(arquivo))

}
func main() {
	exibirIntroducao()
	for {
		exibirMenu()

		cmd := lerComando()

		switch cmd {
		case 1:
			iniciarMonitoramento()
		case 2:
			fmt.Println(("Exibindo logs ..."))
			imprimirLog()
		case 0:
			fmt.Println(("Saindo do programa ..."))
			os.Exit(0)
		default:
			fmt.Print("Comando não encontrado \n")
			os.Exit(-1)
		}
	}

}
