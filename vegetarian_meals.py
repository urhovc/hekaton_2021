while True:


    a = input('Do you want to proceed? Type "y" for yes and "n" for no. If you type "n", the program will close ')

    if a == 'y':
        print('How many people are eating?')
        b = int(input())
 
        number = 0.25 * b
        num1 = 50 * b
        num2 = 2 * b
        num3 = 0.5 * b
        num4 = 250 * b 
        num5 = 60 * b
        num6 = 10 * b 
        num7 = 100 * b 
        num8 = 0,125 * b
        num9 = 80 * b
        num10 = 15 * b
        num11 = 30 * b
        num12 = 25 * b 
        num13 = 2 * b  

        print('Which meal will you eat? Type 1 for breakfast, 2 for lunch and 3 for dinner')
        c = input()

        if c == '1':
            print('You can choose between poached eggs and eggy chese crumpets.')
            d = input('Type 1 for eggs and 2 for crumpets ')

            if d == '1':
                print('You chose poached eggs. You will need:')
                print(b + ' tablespoons of oil')
                print(num3 + 'g chopped kale')
                print(number + ' tablespoons chili flakes')
                print(b + ' large eggs')
                print(b + ' slices multigrain bread')
                print(num12 + 'g halved cherry tomatoes')
                print(num6 + 'g crumbled feta cheese')

                print('STEP 1')
                print('Bring a large pan of water to the boil. Heat the oil in a frying pan over a medium heat and add the kale, \n garlic and chilli flakes. Cook, stirring occasionally, for 4 mins until the kale begins to crisp and wilt to half its size. Set aside.')
                print('STEP 2')
                print('Adjust the heat so the water is at a rolling boil, then poach your eggs for 2 mins. Meanwhile, toast the bread.')
                print('STEP 3')
                print('Remove the poached eggs with a slotted spoon and top each piece of toast with half the kale, an egg, the cherry tomatoes and feta. ')

            if d == '2':
                print('You chose eggy cheese crumpets. You wil need:')
                print(b + ' eggs')
                print(num10 + 'ml milk')
                print(num13 + ' crumpets')
                print(num9 + 'g halved cherry tomatoes')
                print('drizzle of vegetable oil')
                print(num10 + 'g grated cheddar cheese')
                print(b ' small avocados')

                print('STEP 1')
                print('Heat the grill. Beat the eggs and milk together in a wide dish. \n Submerge the crumpets in the egg mixture, turning them once, then set aside for a few minutes.')
                print('STEP 2')
                print('Arrange the tomatoes cut-side up on a baking tray and grill for a few \n minutes, then cover the tray with foil to keep the tomatoes warm.')
                print('STEP 3')
                print('Heat the oil in a frying pan and cook the crumpets for a few minutes on each \n side until the egg has set – you may have to do this in batches. Transfer them to a baking tray as you go. \n Once all the crumpets are cooked, top with the cheese and grill for 1-2 mins until the cheese is bubbling and golden. \n Serve with the tomatoes and avocado slices.')

        if c == '2':
            print('')