def helper(data) -> "":
  match data:
    case "help" or "?":
      return "Help is a command which gives a list of commands that can be run."
    case "exit":
      return "Exits from the application"
    case "banner":
      return "Prints the metaspliot banner"
    case "connectivity":
      return "Checks if internet access is available"
    case _:
        return "Sorry unknown command, it can't be helped"
