with open("z10.txt", 'r') as file:
    lines = file.readlines()
    total_lines = len(lines)
    current_line = 0

    for i in range(0, total_lines, 5):
        chunk = lines[i:i + 5]
        print("".join(chunk))

        if i + 5 < total_lines:
            input("Press Enter to display the next 5 lines...")

        print("End of file.")

