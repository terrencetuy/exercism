defmodule BoutiqueInventory do
  def sort_by_price(inventory) do
    Enum.sort_by(inventory, &(&1.price))
  end

  def with_missing_price(inventory) do
    Enum.filter(inventory, &(&1.price == nil))
  end

  def update_names(inventory, old_word, new_word) do
    Enum.map(inventory, &(
      %{
        price: &1.price,
        name: String.replace(&1.name, old_word, new_word),
        quantity_by_size: &1.quantity_by_size
      }
    ))
  end

  def increase_quantity(item, count) do
      %{
        price: item.price,
        name: item.name,
        quantity_by_size: Map.new(item.quantity_by_size, fn {k, v} -> {k, v + count} end) 
      }
  end

  def total_quantity(item) do
    Enum.reduce(item.quantity_by_size, 0, fn {k, v}, acc -> acc + v end)
  end
end
