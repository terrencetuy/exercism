defmodule BasketballWebsite do
  def extract_from_path(data, path), do:
    extract_from_path_list(data, String.split(path, "."))

  defp extract_from_path_list(data, []), do: data
  defp extract_from_path_list(data, [key | rest_path]), do:
    extract_from_path_list(data[key], rest_path)

  def get_in_path(data, path), do: get_in(data, String.split(path, "."))
end
