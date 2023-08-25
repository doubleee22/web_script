import Foundation

func runCommands(commands: [String]) -> String? {
    let task = Process()
    task.launchPath = "/usr/bin/env"

    let pythonPath = "YOUR PATH TO TENDER_SCRIPT FOLDER"
    let pythonEnv = [
        "PYTHONPATH": pythonPath
    ]
    task.environment = pythonEnv

    task.arguments = ["bash", "-c", commands.joined(separator: " && ")]

    let pipe = Pipe()
    task.standardOutput = pipe
    task.launch()

    let data = pipe.fileHandleForReading.readDataToEndOfFile()
    let output = String(data: data, encoding: .utf8)

    return output
}

let commands = [
    "cd YOUR PATH TO TENDER_SCRIPT FOLDER",
    "python3 main.py"
]

let result = runCommands(commands: commands)
print(result ?? "")
