
def main():

    dial_codes = {
        880 : 'Bangladesh',
        55 : 'Brazil',
        86 : 'China',
        91 : 'India',
        62 : 'Indonesia',
        81 : 'Japan',
        234 : 'Nigeria',
        92 : 'Pakistan',
        7 : 'Russia',
        1 : 'United States',
    }

    print("\nPrint the value (code) of the key variable: ")
    for key in dial_codes:
        print(key)
    
    print("\nPrint the value (country) that is assosiated with key: ")
    for key in dial_codes:
        print(dial_codes[key])
    
    print("\nPrint the key variable (code) followed by the value (country) that is assosiated with that key: ")
    for key in dial_codes:
        print(key, dial_codes[key])
    
    print("\nPrint the dictionary")
    print(dial_codes)

main()