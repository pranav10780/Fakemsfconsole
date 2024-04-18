def helper(data) -> "":
  match data:
    case "help":
      return "\nHelp is a command which gives a list of commands that can be run.\n"
    case "exit":
      return "\nExits from the application\n"
    case "banner":
      return "\nPrints the metaspliot banner\n"
    case "connectivity":
      return "\nChecks if internet access is available\n"
    case "version":
      return "\nShow the verdion\n"
    case _:
        return "\nSorry unknown command, it can't be helped\n"
