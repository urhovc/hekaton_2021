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
        num14 = 150 * b 
        num15 = 20 *b

        print('Which meal will you eat? Type 1 for breakfast, 2 for lunch and 3 for dinner')
        c = input()

        if c == '1':
            print('You can choose between vegan pancakes and banana baked oatmeal.')
            d = input('Type 1 for pancakes and 2 for oatmeal ')

            if d == '1':
                print('You chose vegan pancakes. You will need:')
                print(str(num9) + 'g self raising flour')
                print(str(number) + ' tablespoons baking powder')
                print(str(number) + ' tablespoons sugar')
                print(str(num7) + 'ml plant based milk')
                print(str(number) + ' tablespoons vegetable oil for cooking')

                print('STEP 1')
                print('Whisk the flour, baking powder, sugar, vanilla extract and a pinch of salt in a bowl using a balloon whisk until mixed. \n Slowly pour in the milk until you get a smooth, thick batter.')
                print('STEP 2')
                print('Heat a little of the oil in a non-stick frying pan over a medium-low heat, and add 2 tbsp batter into the pan at a time to make small,\n round pancakes. You will need to do this in batches of two-three at a time. Cook for 3-4 mins until the edges are set, \n and bubbles are appearing on the surface. Flip the pancakes over and cook for another 2-3 mins until golden on both sides and cooked through. \n Keep warm in a low oven while you cook the remaining pancakes. ')
                print('STEP 3')
                print('Serve stacked with lots of toppings of your choice, or serve with bowls of toppings for everyone to help themselves. ')

            if d == '2':
                print('You chose banana baked oatmeal. You will need:')
                print('oats')
                print('cinnamon')
                print('baking powder')
                print(str(num2) + 'bananas')
                print('almond milk')
                print('peanut butter')
                print('maple syrup')
                print('ground flaxseed')
                print('vanilla extract')

                print('STEP 1')
                print('Start by mashing two ripe bananas in a bowl. Then add the wet ingredients on top, including the peanut butter, maple syrup, \n ground flaxseed (which combined with liquid replaces the egg) along with almond milk. Mix it all together until well combined.')
                print('STEP 2')
                print('Put the dry ingredients including the oats, cinnamon baking powder and salt, into a baking dish like this one and whisk them \n together with a fork. Pour the wet on top of the oats mixture and stir to combine. Bake in a pre heated oven until the mixture is set.')
                print('STEP 3')
                print('When it comes out of the oven, you’ll notice the sides of the baking dish are browned and the banana baked oatmeal pulls away from the sides. \n That’s when you know it’s done! I love to add a drizzle of peanut butter and some banana slices to serve the oatmeal … delicious!')

        if c == '2':
            print('You can have vegan fajitas.')
            e = input('Type 1 for fajitas ')
        
            if e == '1':
                print('You chose vegan fajitas. You will need:')
                print(str(number) + ' tablespoons vegetable oil')
                print(str(num3) + ' red or yellow peppers')
                print(str(number) + ' sliced red onions')
                print(str(number) + ' garlic cloves, crushed')
                print(str(num8) + ' tablespoons of chili powder or flakes')
                print(str(num8) + ' tablespoons of ground paprika')
                print(str(num8) + ' tablespoons of ground cumin')
                print('juice of ' + str(number) + ' limes')
                print(str(num7) + 'g black beans')
                print(str(b) + ' tortillas')
                print('small bunch of coriander, finely chopped')
                print(str(num3) + ' avocados, sliced')
                print('dairy free yogurt to serve with (optional)')

                print('STEP 1')
                print('Heat the oil in a frying pan and fry the peppers and onions over a medium high heat until tender and starting to turn golden brown, \n about 6-8 mins. Add the garlic and spices and fry for 1 min more until fragrant. Add half of the lime juice and season.\n Transfer to a serving dish and keep warm while you heat the beans.')
                print('STEP 2')
                print('Tip the black beans into the same frying pan and add the remaining lime juice. Season well, and stir until warmed through and coated \n in any remaining spices from the pan. Stir in most of the coriander.')
                print('STEP 3')
                print('Warm the tortillas in the microwave or wrapped in foil in a low oven, then cover with a tea towel to keep them warm.\n Serve the wraps with the peppers, beans, avocado, dairy-free yogurt, extra coriander and extra lime wedges to squeeze over, if you like.  ')

        if c == '3':
            print('You can have a vegan burger.')
            f = input('Type 1 for burger. ')

            if f == '1':
                print('You chose the vegan burger. You will need:')
                print(str(number) + ' tablespoons olive oil')
                print(str(num8) + ' leeks, chopped')
                print(str(b) + ' mushrooms, chopped')
                print(str(num6) + 'g picked thyme leaves')
                print(str(num11) + 'g firm tofu')
                print(str(number) + ' handfuls of kale leaves')
                print(str(number) + ' tablespoons of Dijon mustard')
                print(str(num3) + ' tablespoons tamari')
                print(str(num5) + 'g canned black beans, drained')
                print(str(b) + ' tablespoons of oat bran')
                print(str(num3) + ' tablespoons of cooked brown')
                print(str(num3) + ' tablespoons chopped hazelnuts or ')
                print(str(num6) + 'g flour')
                print(str(b) + ' burger buns')
                print(str(b) + ' tablespoons vegan mayo')
                print(str(number) + ' tablespoons ketchup')
                print(str(number) + ' tablespoons of chopped cornichons')
                print('pinch of cayenne pepper')
                print('sliced tomatoes and red onions')
                print('lettuce leaves')

                print('STEP 1')
                print('Heat the oil in a large pan and fry the leek, mushrooms, thyme, tofu and kale for about 5 mins. \n Add the mustard, tamari and half of the black beans and give it a good stir. Transfer the mixture to a blender and pulse a few times \n– don’t over-blend, it needs to be quite chunky in texture. Scoop into a bowl and add the \n rest of the black beans, the oat bran, rice and chopped nuts, then mix well.')
                print('STEP 2')
                print('Divide the mixture into 4-6 evenly sized portions and shape into patties using your hands. \n Tip the gram flour onto a plate, if using, then roll the patties in the flour to coat.')
                print('STEP 3')
                print('To make the burger dressing, mix all ingredients together in a bowl and set aside. \n Fry the patties for 4-5 mins on each side until crisp on the outside.')
                print('STEP 4')
                print('Slide the patties into the buns with the tomato, onion, lettuce and a dollop of burger dressing.')