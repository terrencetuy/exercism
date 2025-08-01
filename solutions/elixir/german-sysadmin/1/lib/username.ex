defmodule Username do
  def sanitize([]), do: []
  def sanitize([first_letter | rest]) do
    case first_letter do
      first_letter when first_letter >= ?a and first_letter <= ?z -> [first_letter]
      first_letter when first_letter == ?_ -> [first_letter]
      first_letter when first_letter == ?ä -> [?a, ?e]
      first_letter when first_letter == ?ö -> [?o, ?e]
      first_letter when first_letter == ?ü -> [?u, ?e]
      first_letter when first_letter == ?ß -> [?s, ?s]
      _ -> []
    end
    |> Kernel.++(sanitize(rest))
  end
end
