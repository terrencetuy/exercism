defmodule HighScore do
  @default_initial_score 0

  def default_initial_score(), do: @default_initial_score

  def new(), do: Map.new()

  def add_player(scores, name, score \\ default_initial_score()), do: Map.put(scores, name, score)

  def remove_player(scores, name), do: Map.delete(scores, name)

  def reset_score(scores, name), do: add_player(scores, name)

  def update_score(scores, name, score), do: Map.update(scores, name, default_initial_score() + score, &(&1 + score))

  def get_players(scores), do: Map.keys(scores)
end
