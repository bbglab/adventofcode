package main

import (
	"bufio"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {

	// Open file
	fd, err := os.Open("./input.txt")
	if err != nil {
		log.Fatalf("Error opening the file. %v", err)
	}
	defer fd.Close()

	// Load passports
	passport := make(map[string]string)
	passports := make([]map[string]string, 0)
	scanner := bufio.NewScanner(fd)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		println(line)
		if line == "" {
			passports = append(passports, passport)
			passport = make(map[string]string)
		} else {
			fields := strings.Split(line, " ")
			for _, field := range fields {
				valKey := strings.Split(field, ":")
				passport[valKey[0]] = valKey[1]
			}
		}
	}
	if len(passport) > 0 {
		passports = append(passports, passport)
	}

	// Count valid passports
	countPartOne := 0
	countPartTwo := 0
	for _, passport := range passports {
		if validPassportPartOne(passport) {
			countPartOne += 1
		}
		if validPassportPartTwo(passport) {
			countPartTwo += 1
		}
	}

	// Output results
	println("Total valid passports part one:", countPartOne)
	println("Total valid passports part two:", countPartTwo)
}

var required = []string{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

func validPassportPartOne(passport map[string]string) bool {
	for _, key := range required {
		if _, ok := passport[key]; !ok {
			return false
		}
	}
	return true
}

func validPassportPartTwo(passport map[string]string) bool {
	for _, key := range required {
		if value, ok := passport[key]; !ok {
			return false
		} else {
			switch key {
			case "byr":
				if !validFourDigitNumber(value, 1920, 2002) {
					return false
				}

			case "iyr":
				if !validFourDigitNumber(value, 2010, 2020) {
					return false
				}

			case "eyr":
				if !validFourDigitNumber(value, 2020, 2030) {
					return false
				}

			case "hgt":
				if !validHeight(value) {
					return false
				}

			case "hcl":
				if !validHairColor(value) {
					return false
				}

			case "ecl":
				if !validEyeColor(value) {
					return false
				}

			case "pid":
				if !validPassportID(value) {
					return false
				}
			}
		}
	}
	return true
}

func validPassportID(value string) bool {
	m, err := regexp.MatchString("^[0-9]{9}$", value)
	return err == nil && m
}

var eyeColors = map[string]bool{"amb": true, "blu": true, "brn": true, "gry": true, "grn": true, "hzl": true, "oth": true}

func validEyeColor(value string) bool {
	r, ok := eyeColors[value]
	return ok && r
}

func validHairColor(value string) bool {
	m, err := regexp.MatchString("^#[0-9a-f]{6}$", value)
	return err == nil && m
}

func validHeight(value string) bool {
	suffix := value[len(value)-2:]
	num, err := strconv.Atoi(value[:len(value)-2])
	if err != nil {
		return false
	}
	switch suffix {
	case "cm":
		return num >= 150 && num <= 193
	case "in":
		return num >= 59 && num <= 76
	}
	return false
}

func validFourDigitNumber(value string, from int, to int) bool {
	if len(value) != 4 {
		return false
	}
	v, err := strconv.Atoi(value)
	if err != nil || v < from || v > to {
		return false
	}
	return true
}
