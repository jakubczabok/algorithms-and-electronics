# This Julia code parses a PGN file containing chess games, filters the games based on specific criteria and saves the filtered games to a new file

function parse_pgn(file_path::String)
    games = String[]
    open(file_path, "r") do io
        current_game = String[]
        for line in eachline(io)
            stripped_line = strip(line)
            if isempty(stripped_line) && !isempty(current_game)
                push!(games, join(current_game, "\n"))
                empty!(current_game)
            elseif !isempty(stripped_line)
                push!(current_game, line)
            end
        end
        if !isempty(current_game)
            push!(games, join(current_game, "\n"))
        end

        filtered_games = filter_games(games)
        return filtered_games
    end
end

function filter_games(games::Vector{String})
    filtered_games = String[]
    for game in games
        if is_game_valid(game)
            push!(filtered_games, game)
        end
    end
    return filtered_games
end

function is_game_valid(game::String)
    white_elo_match = match(r"\[WhiteElo \"([^\"]*)\"\]", game)
    result_match = match(r"\[Result \"([^\"]*)\"\]", game)

    if isnothing(white_elo_match) || isnothing(result_match)
        return false
    end

    try
        white_elo = parse(Int, white_elo_match.captures[1])
        result = result_match.captures[1]

        if !(2000 <= white_elo <= 2700)
            return false
        end

        if !(result in ["1-0", "0-1"])
            return false
        end

        return true
    catch e
        println("Error parsing Elo: ", e)
        return false
    end
end

function save_filtered_games(file_path::String, games::Vector{String})
    open(file_path, "w") do io
        for game in games
            write(io, game * "\n\n")
        end
    end
end

input_file = "C:/Users/jczab/Downloads/Duda/Duda.pgn"
output_file = "filtered_games.pgn"

try
    parsed_games = parse_pgn(input_file)
    save_filtered_games(output_file, parsed_games)
    println("Filtered games saved to '$output_file'")
catch e
    println("Error occured: ", e)
end
