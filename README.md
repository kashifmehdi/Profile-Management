# Profile Management Program 📝

## Overview ℹ️
The Profile Management Program is a menu-driven application designed to manage social profiles. It allows users to perform various operations on personal profile information stored in a text file. Users can interactively query and manipulate the profile information using simple commands until they choose to quit the program.

## Table of Contents 📋
- [Introduction](#introduction)
- [Technologies](#technologies)
- [Input Data](#input-data)
- [Interactive Mode](#interactive-mode)
  - [Summary](#summary)
  - [Add](#add)
  - [Remove](#remove)
  - [Search](#search)
  - [Update](#update)
  - [Quit](#quit)

## Introduction 🚀
The Profile Management Program is a Python-based application that facilitates the management of personal profile information within a simple social network. It utilizes a menu-driven interface to provide users with easy access to various functionalities for manipulating profile data.

## Technologies 💻
The project is developed using:
- Python version: 3.8

## Input Data 📥
The program starts by reading personal profile information from a file named `profiles.txt`. This file contains profile details such as given name, family name, email address, and gender. Each profile's information is stored on a separate line and separated by spaces.

## Interactive Mode 💬
Once the initial profile data is loaded, the program enters an interactive mode where users can execute commands to interact with the profile information. Below are the available commands:

### Summary 📄
- **Description**: Outputs the contents of the profile list.
- **Usage**: `Summary`

### Add ➕
- **Description**: Prompts for a person’s email address. If the email address does not already exist in the profile list, it prompts for and reads the person’s details (given name, family name, gender, and status) and adds the information to the profile list.
- **Usage**: `Add`

### Remove ❌
- **Description**: Prompts for a person’s email address. If the email address is found in the profile list, it removes the corresponding profile from the list.
- **Usage**: `Remove`

### Search 🔍
- **Description**: Prompts for a person’s email address and searches for the person in the profile list. If found, it displays the person’s details; otherwise, it shows an error message.
- **Usage**: `Search`

### Update 🔄
- **Description**: Prompts for a person’s email address. If the email address is found in the profile list, it allows updating the person’s details such as given name, family name, status, adding a friend, or removing a friend.
- **Usage**: `Update`

### Quit 🛑
- **Description**: Exits the program and outputs the contents of the profile list (list of profile objects) to a file.
- **Usage**: `Quit`

This README provides an overview of the Profile Management Program and its functionalities, guiding users on how to interact with the application effectively.
