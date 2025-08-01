defmodule RPG.CharacterSheet do
  def welcome() do
    IO.puts("Welcome! Let's fill out your character sheet together.")
    :ok
  end

  def ask_name(), do: prompt("What is your character's name?\n")

  def ask_class(), do: prompt("What is your character's class?\n")

  def ask_level() do
    prompt("What is your character's level?\n")
    |> String.to_integer()
  end

  def run() do
    welcome()
    name = ask_name()
    class = ask_class()
    level = ask_level()
    character_sheet = %{
      class: class,
      level: level,
      name: name
    }
    |> IO.inspect(label: "Your character")
  end

  defp prompt(label) do
    IO.gets(label)
    |> String.trim()
  end
end
