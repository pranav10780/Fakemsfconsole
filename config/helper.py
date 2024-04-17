def helper(data) -> "":
  match data:
    case "help":
      return "Help is a command which gives a list of commands that can be run."
    case _:
        return "Sorry unknown command, it can't be helped"
