package main

import (
	"fmt"
)

type user struct {
	name  string
	email string
	ext   int
	priv  bool
}

type admin struct {
	pserson user
	level   string
}

func main() {
	lise := user{
		name:  "lise",
		email: "email",
		ext:   123,
		priv:  true,
	}

}

func removeColor(colors map[string]string, key string) {
	delete(colors, key)
}
func foo(slice []int) []int {
	// return fmt.Println(slice[1:3])
	return nil
}

func printMap(c map[string]string) {
	for key, value := range c {
		fmt.Println("hex code for", key, "is", value)
	}
}

func getGreeting(text string) {
	fmt.Println(text)
}

func (ip IP) MarchelText() ([]byte, error) {
	if len(ip) == 0 {
		return []byte(""), nil
	}

	if len(ip) != IPv4len && len(ip) != IPv4len {
		return nil, errors.New("invalid IP Address")
	}
	return []byte(ip.String()), nil
}

func ipEmpty(ip IP) string {
	if len(ip) == 0 {
		return " "
	}

	return ip.String()
}

func Now() Time {
	sec, nsec := now()
	return Time{sec + unixToInternal, nsec, Local}
}
