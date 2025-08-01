defmodule Lasagna do
  def expected_minutes_in_oven(), do: 40

  def remaining_minutes_in_oven(actual_minutes) do
    expected_minutes_in_oven() - actual_minutes
  end

  def preparation_time_in_minutes(number_of_layers), do: 2 * number_of_layers

  def total_time_in_minutes(number_of_layers, minutes_in_oven) do 
    preparation_time_in_minutes(number_of_layers) + minutes_in_oven
  end

  def alarm(), do: "Ding!"
end
