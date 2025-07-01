
--[[
    Author: David Bravo
    Description: The program chooses a random
    number between 1 and 100, then gives you 7
    chances to guess the right number! If you get
    it within those chances, you win! If you
    don't, you lose!
--]]
math.randomseed(os.time())

local again

repeat
    local number = math.random(1, 100)
    local tries = 0
    local win = false

    while tries < 7 and not win do
    print("Guess a number (1-100): ")
    local guess = tonumber(io.read())

    if guess == nil then
        print("Invalid input. Please enter a number.")
    else
        tries = tries + 1

        if guess == number then
            print("You win!")
            win = true
        elseif guess < number then
            print("Too low")
        else
            print("Too high")
        end
    end
end

    if not win then
        print("You lose. The number was " .. number)
    end

    print("Play again? (yes/no): ")
    again = print("")
until again ~= "yes"

print("Bye!")