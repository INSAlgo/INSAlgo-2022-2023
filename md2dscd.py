# Change classic markdown into inferior, digshit discord markdown for easier broadcast

md_name = "README.md"
dc_name = "Discord.txt"

repo_link = "https://github.com/INSAlgo/INSAlgo-2022-2023/blob/main/"

def convert(folder: str) :
    try :
        File = open(folder + '/' + md_name)
    except :
        return 1
    try :
        Dest = open(folder + "/" + dc_name, mode="w")
    except :
        return 2
    
    lines = File.readlines()
    File.close()

    for i in range(len(lines)) :
        
        # Format slides :
        if lines[i].startswith("[slides]") :
            Dest.write("__Slides__\n")
            Dest.write("  - " + repo_link + folder + '/' + lines[i][9:-2] + '\n')
            continue
        
        # Format Exercice title :
        if lines[i] == "## Exercices\n" :
            lines[i] = "__Exercices__\n"
        
        # Format levels :
        if lines[i].startswith("### Level") :
            lines[i] = "Lvl " + lines[i][-2]
        
        # Format exercises :
        if "[Solution]" in lines[i] :
            i1, i2, i3 = lines[i].find("]("), lines[i].find(") "), lines[i].find(" : ")
            lines[i] = "  - " + lines[i][3:i1] + " : " + lines[i][i1+2:i2] + lines[i][i2+1:i3] + "\n"
        
        # Fixing line jumps :
        lines[i].replace("</br>\n", "\n")
        lines[i].replace("</br>", "\n")

        # Format title :
        if lines[i].startswith("# ") :
            lines[i] = "**" + lines[i][2:-1] + "**\n\n"
        
        Dest.write(lines[i])

    Dest.write("\n__Solutions__\n\n" + repo_link + folder)

    Dest.close()
    return 0

if __name__ == "__main__" :
    error = convert("08 - Libraries")
    if error == 1 :
        print("Could not open markdown")
    elif error == 2 :
        print("Could not open destination file")
    