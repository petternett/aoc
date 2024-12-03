defmodule Aoc1 do
  def do_1a do
    File.read!("input")
    |> String.split("\n", trim: true)
    |> Enum.map(&String.split/1)
    |> Enum.reduce({[], []}, fn [first, second], {a, b} ->
      {[first | a], [second | b]}
    end)
    |> then(fn {l1, l2} -> {Enum.sort(l1), Enum.sort(l2)} end)
    |> then(&Enum.zip(elem(&1, 0), elem(&1, 1)))
    |> Enum.reduce([], fn {x, y}, acc ->
      [abs(String.to_integer(x) - String.to_integer(y)) | acc]
    end)
    |> Enum.sum()
  end

  def do_1b do
    File.read!("input")
    |> String.split("\n", trim: true)
    |> Enum.map(&String.split/1)
    |> Enum.reduce({[], []}, fn [first, second], {a, b} ->
      {[first | a], [second | b]}
    end)
    |> then(fn {lst_a, lst_b} ->
      Enum.map(lst_a, fn x ->
        String.to_integer(x) * Enum.count(lst_b, fn y -> y == x end)
      end)
    end)
    |> Enum.sum()
  end
end

Aoc1.do_1a() |> IO.inspect(label: "A")
Aoc1.do_1b() |> IO.inspect(label: "B")
