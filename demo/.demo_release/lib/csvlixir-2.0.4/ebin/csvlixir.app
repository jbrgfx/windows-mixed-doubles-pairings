{application,csvlixir,
             [{applications,[kernel,stdlib,elixir]},
              {description,"CSVLixir is a CSV reader/writer for Elixir.\n\nReading from files returns a stream of lists. Reading from strings returns a\nlist of lists.\n\nThe writer transforms a (possibly lazy) list of lists into a stream of CSV\nstrings. It can also take a single list and return a single CSV string.\n"},
              {modules,['Elixir.CSVLixir','Elixir.CSVLixir.FileReader',
                        'Elixir.CSVLixir.IOReader',
                        'Elixir.CSVLixir.StringReader',
                        'Elixir.CSVLixir.Writer']},
              {registered,[]},
              {vsn,"2.0.4"}]}.
