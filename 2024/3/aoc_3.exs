defmodule Aoc3 do
  def do_3a do
    ~r/mul\((?<x>\d{1,3}),(?<y>\d{1,3})\)/
    |> Regex.scan(File.read!("input"), capture: :all_names)
    |> Enum.reduce(0, fn [x, y], acc ->
      String.to_integer(x) * String.to_integer(y) + acc
    end)
  end

  defp process([], sum, _check), do: sum

  defp process([["do()"] | tail], sum, _check) do
    process(tail, sum, true)
  end

  defp process([["don't()"] | tail], sum, _check) do
    process(tail, sum, false)
  end

  defp process([[x, y] | tail], sum, true) do
    case {Integer.parse(x), Integer.parse(y)} do
      {{n1, _}, {n2, _}} -> process(tail, sum + n1 * n2, true)
      _ -> process(tail, sum, true)
    end
  end

  defp process([_head | tail], sum, false) do
    process(tail, sum, false)
  end

  def do_3b do
    ~r/mul\((?<x>\d{1,3}),(?<y>\d{1,3})\)|(?<yes>do\(\))|(?<no>don\'t\(\))/
    |> Regex.scan(File.read!("input"), capture: :all_names)
    |> Enum.map(&Enum.reject(&1, fn x -> x == "" end))
    |> process(0, true)
  end
end

Aoc3.do_3a() |> IO.inspect(label: "A", charlists: :as_lists)
Aoc3.do_3b() |> IO.inspect(label: "B", charlists: :as_lists)
