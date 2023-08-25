def convert(main):
    main = main.replace(":(","🙁").replace(":)", "🙂")
    print(main)

main = input(f"Write the following sentence:\n\"I say, \"Yes\" :), you say \"No\" \n\"You say \"Stop\", and I say \"Go, go, go\"\" ")

convert(main)