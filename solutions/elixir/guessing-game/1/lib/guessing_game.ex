defmodule GuessingGame do
  def compare(secret_number, guess \\ :no_guess) do
    cond do
      guess === :no_guess -> "Make a guess"
      secret_number === guess -> "Correct"
      abs(guess - secret_number) == 1 -> "So close"
      guess > secret_number -> "Too high"
      guess < secret_number -> "Too low"
    end
  end
end
