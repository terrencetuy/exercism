defmodule BirdCount do
  def today([]), do: nil
  def today(list),  do: hd(list)

  def increment_day_count([]), do: [1]
  def increment_day_count(list), do: [today(list) +1 | tl(list)]

  def has_day_without_birds?([]), do: false
  def has_day_without_birds?(list), do: today(list) === 0 or has_day_without_birds?(tl(list))

  def total([]), do: 0
  def total(list), do: today(list) + total(tl(list))

  def busy_days([]), do: 0
  def busy_days(list) do
    cond do
      today(list) >= 5 -> 1 + busy_days(tl(list))
      true -> busy_days(tl(list))
    end
  end
end
