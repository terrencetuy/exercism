defmodule BasketballWebsite do
  def extract_from_path(data, path) do
    path_list = String.split(path, ".")
    extract_from_path_list(data, path_list)
  end

  defp extract_from_path_list(data, []), do: data
  defp extract_from_path_list(data, [head_path | rest_path]), do:
    extract_from_path_list(data[head_path], rest_path)

  def get_in_path(data, path) do
    path_list = String.split(path, ".")
    get_in(data, path_list)
  end
end
