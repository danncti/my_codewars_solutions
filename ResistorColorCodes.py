def encode_resistor_colors(ohms_string):
    colors = {0: "black", 1: "brown", 2: "red", 3: "orange", 4: "yellow", 5: "green", 6: "blue", 7: "violet", 8: "gray", 9: "white"}

    ohms = ohms_string.replace(" ohms", "")
    ohms_mult = 1
    if "k" in ohms:
        ohms_mult = 1000
        ohms = ohms.replace("k", "")
    elif "M" in ohms:
        ohms_mult = 1000000
        ohms = ohms.replace("M", "")

    ohms = int(float(ohms)*ohms_mult)
    d  = [int(i) for i in str(ohms) if i.isdigit()]
    return " ".join([colors[d[0]], colors[d[1]], colors[len(str(ohms))-2], "gold"])

# below - not in the answer
def main():

    assert encode_resistor_colors("10 ohms") == "brown black black gold"
    assert encode_resistor_colors("4.7k ohms") == "yellow violet red gold"
    assert encode_resistor_colors("1M ohms") == "brown black green gold"


if __name__ == "__main__":
        main()