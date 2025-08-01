defmodule KitchenCalculator do
  @milliliters_per_cup 240
  @milliliters_per_fluid_ounce 30
  @milliliters_per_teaspoon 5
  @milliliters_per_tablespoon 15

  def get_volume(volume_pair) do
    elem(volume_pair, 1)
  end

  def to_milliliter({:milliliter, _} = volume_pair), do: volume_pair
  def to_milliliter({:cup, volume} = volume_pair), do: {:milliliter, @milliliters_per_cup * volume}
  def to_milliliter({:fluid_ounce, volume} = volume_pair), do: {:milliliter, @milliliters_per_fluid_ounce * volume}
  def to_milliliter({:teaspoon, volume} = volume_pair), do: {:milliliter, @milliliters_per_teaspoon * volume}
  def to_milliliter({:tablespoon, volume} = volume_pair), do: {:milliliter, @milliliters_per_tablespoon * volume}
                    
  def from_milliliter(volume_pair, unit = :milliliter), do: volume_pair
  def from_milliliter(volume_pair, unit = :cup), do: {unit, get_volume(volume_pair) / @milliliters_per_cup}
  def from_milliliter(volume_pair, unit = :fluid_ounce), do: {unit, get_volume(volume_pair) / @milliliters_per_fluid_ounce}
  def from_milliliter(volume_pair, unit = :teaspoon), do: {unit, get_volume(volume_pair) / @milliliters_per_teaspoon}
  def from_milliliter(volume_pair, unit = :tablespoon), do: {unit, get_volume(volume_pair) / @milliliters_per_tablespoon}

  def convert(volume_pair, unit) do
    to_milliliter(volume_pair)
    |> from_milliliter(unit)
  end
end
