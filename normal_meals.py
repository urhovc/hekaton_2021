while True:
    a = input('Do you want to proceed? Type "y" for yes and "n" for no. If you type "n", the program will close ')

    if a == 'y':
        print('How many people are eating?')
        b = int(input())
        print('Which meal will you eat? Type 1 for breakfast, 2 for lunch and 3 for dinner')
        c = input()

        if c == '1':
            print('You have to choose between overnight oats (requires some prep work the night before) and avocado toast.')
            d = input('Type 1 for oats and 2 for toast ')

            if d == '1':
                number = 0.25 * b
                num1 = 50 * b
                num2 = 2 * b
                num3 = 0.5 * b
                print('You chose overnight oats. You will need:')
                print(str(number) + ' tablespoons cinnamon')
                print(str(num1) + 'g rolled porridge oats')
                print(str(num2) + ' tablespoons natural yogurt')
                print(str(num1) +  'g mixed berries')
                print(str(b) + ' drizzle(s) of honey')
                print(str(num3) + ' tablespoons of nut butter')

                print('STEP 1')
                
                print('The night before serving, stir the cinnamon and 100ml water (or milk) into your oats with a pinch of salt.')
                
                print('STEP 2')
                print('The next day, loosen with a little more water (or milk) if needed. Top with the yogurt, berries, a drizzle of honey and the nut butter.')
            
            if d == '2':
                print('You chose avocado toast. you will need:')
                print(num3 + ' avocado(s), seeded and peeled')
                print(b + 'tablespoons of chopped cilantro')