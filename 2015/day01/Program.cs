using System.IO;

string path = Path.Combine(Directory.GetCurrentDirectory(), "input.txt");

string contents = File.ReadAllText(path);

int counter = 0;

// Part 1
foreach (char c in contents)
{
    if (c == '(')
    {
        counter++;
    }
    else if (c == ')')
    {
        counter--;
    }
}

Console.WriteLine(counter);

// Part 2
int position = 0;
int counter2 = 0;
int index = 0;

foreach (char c in contents)
{
    index++;

    if (c == '(')
    {
        counter2++;
    }
    else if (c == ')')
    {
        counter2--;

        if (counter2 < 0)
        {
            position = index;
            break;
        }
    }
}

Console.WriteLine(position);
