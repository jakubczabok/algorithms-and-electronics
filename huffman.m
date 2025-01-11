% This MATLAB code simulates Huffman compression on randomly generated text strings of varying lengths, it calculates and displays entropy and compression ratio for each text length 

clc; clear;

alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','y','w','z','x','0','1','2','3','4','5','6','7','8','9',' '};

function H = ComputeEntropy(s)
    if (ischar(s))
        l = strlength(s);
        uniqueChars = unique(s);
        lenChar = strlength(uniqueChars);
        f = zeros(1, lenChar);
        for i = 1 : lenChar
            f(i) = sum(s == uniqueChars(i));
        end
        p = f / l;
        p = p(p>0); % remove zero probabilities
        if isempty(p)
            H = 0;
        else
            H = -sum(p .* log2(p));
        end
    else
        display('Invalid String');
        H = NaN;
    end
end

textLengths = [10, 25, 50, 100, 200, 500, 1000];
results = [];

for textLength = textLengths
    a = 1;
    b = size(alphabet, 2);
    r = randi([a, b], textLength, 1);
    rText = '';
    for i = 1 : textLength
        rText = [rText, alphabet{r(i)}];
    end

    entropy = ComputeEntropy(rText);

    propabilityOfSymbol = zeros(size(alphabet));
    for i = 1:length(alphabet)
        propabilityOfSymbol(i) = sum(rText == alphabet{i});
    end
    propabilityOfSymbol = propabilityOfSymbol / strlength(rText);

    validIndices = propabilityOfSymbol > 0;
    validAlphabet = alphabet(validIndices);
    validProbabilities = propabilityOfSymbol(validIndices);
    
    if ~isempty(validProbabilities)
        [dict, avglen] = huffmandict(validAlphabet, validProbabilities);
    else
        avglen = 0; % handle case where all probabilities are zero
        dict = {};
    end

    fixedCodeLength = ceil(log2(length(alphabet)));
    
    if avglen > 0
        compressionRatio = fixedCodeLength / avglen;
    else
        compressionRatio = NaN; % handle case where avglen is zero
    end

    results = [results; textLength, entropy, avglen, fixedCodeLength, compressionRatio];
end

disp('-----------------------------------------------------------------------------------');
disp('Length | Entropy | Avg. Huffman Code Length | Avg. Fixed Code Length | Compression Ratio');
disp('-----------------------------------------------------------------------------------');
for i = 1:size(results, 1)
    fprintf('%7d | %8.4f | %20.4f | %20.4f | %15.4f\n', results(i, 1), results(i, 2), results(i, 3), results(i, 4), results(i, 5));
end
disp('-----------------------------------------------------------------------------------');
