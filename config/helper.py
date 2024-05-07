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
      return "\nShow the version\n"
    case "history":
      return "\nShows all previously typed commands\n"
    case "save":
      return "\nInstead of showing previous commands it saves them so that it can stayed saved even if the program is closed.\nAlso there is only one file so be careful because you can override existing saved history"
    case "showsaved":
      return "\nShows the command saved by the command save.\nSee \"help save\" for more info\n"
    case _:
        return "\nSorry unknown command, it can't be helped\n"
