defmodule Aoc2 do
  defp check_valid(lst) do
    (lst == Enum.sort(lst) || lst == Enum.reverse(Enum.sort(lst))) &&
      Enum.chunk_every(lst, 2, 1, :discard)
      |> Enum.map(fn [a, b] -> abs(a - b) in 1..3 end)
      |> Enum.all?()
  end

  def do_2a do
    File.read!("input")
    |> String.split("\n", trim: true)
    |> Enum.map(&String.split/1)
    |> Enum.map(&Enum.map(&1, fn x -> String.to_integer(x) end))
    |> Enum.filter(fn report ->
      report
      |> check_valid()
    end)
    |> Enum.count()
  end

  def do_2b do
    File.read!("input")
    |> String.split("\n", trim: true)
    |> Enum.map(&String.split/1)
    |> Enum.map(&Enum.map(&1, fn x -> String.to_integer(x) end))
    |> Enum.filter(fn report ->
      0..(length(report) - 1)
      |> Enum.any?(fn skip_idx ->
        report
        |> Enum.with_index()
        |> Enum.reject(fn {_, idx} -> idx == skip_idx end)
        |> Enum.map(fn {val, _} -> val end)
        |> check_valid()
      end)
    end)
    |> Enum.count()
  end
end

Aoc2.do_2a() |> IO.inspect(label: "A", charlists: :as_lists)
Aoc2.do_2b() |> IO.inspect(label: "B", charlists: :as_lists)
