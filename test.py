"""This files tests the strinpicker module"""

from stringpicker import pick_random, format_output, longest_string

QUESTIONS = ["GULAG", "Magnitogorsk", "The Great Terror",
             "collectivization", "The New Woman", "Fordism", "NSDAP",
             "The Nazi Seizure of Power", "Weimar Republic",
             "Nuremberg Laws", "Anti-Semitism", "The Amritsar Massacre",
             "Mohandas Gandhi", "Marcus Garvey", "Pan-Africanism",
             "The CPC", "Mao Zedong", "Chiang Kai-shek", "The New Deal",
             "Italian-Abyssinian War", "Spanish Civil War", "Rape of Nanking",
             "The Great Depression", "Molotov-Ribbentrop Pact",
             "Battle of Britain", "Blitzkrieg", "Operation Barbarossa",
             "General Plan East", "strategic bombing", "The Warsaw Pact",
             "Pearl Harbor", "Vichy France", "Hungerplan", "Einsatzgruppen",
             "D-Day", "Lebensraum", "The Manhattan Project", "The Long March",
             "The Battle of Stalingrad", "Battle of the Atlantic", "Sputnik",
             "The Battle of Midway", "Battle of Berlin", "Battle of Berlin",
             "Hiroshima", "The Potsdam Conference", "The Yalta Conference",
             "The United Nations", "The Cold War", "The Greek Civil War",
             "Restalinization", "The Truman Doctrine", "Nuclear War", "ICBMs",
             "Civil Defense", "MAD", "The Prague Coup", "NATO", "Death Camp",
             "The PRC", "The Marshall Plan", "The Wirtschaftswunder",
             "The Berlin Airlift", "The Korean War", "Nikita Khrushchev",
             "The Cuban Revolution", "Fidel Castro", "The Berlin Wall",
             "The Reichstag Fire", "Katyn Massacre", "Lend-Lease Aid",
             "The Cuban Missile Crisis", "The Birth of Israel",
             "The 1967 Arab-Israeli War", "Apartheid", "Decolonization",
             "Partition (India, 1947)", "The Non-Aligned Movement",
             "Mau Mau", "The Algerian War", "The Suez Crisis",
             "Gamal Abdel Nasser", "Jwawharlal Nehru", "Kwame Nkrumah",
             "The Year of Africa", "Nelson Mandela", "Dien Bien Ph",
             "The Civil Rights Movement", "The Vietnam War", "Khmer Rouge",
             "Massacre at My Lai", "The Tet Offensive", "The Prague Spring",
             "The Cultural Revolution", "The Long Downturn", "The Oil Crises",
             "OPEC", "The RAF", "The Revolutions of 1968", "Detente",
             "The Sino-Soviet Split", "The Iranian Revolution", "Islamism",
             "Soviet Invasion of Afghanistan", "The European Union",
             "The Third World Debt Crisis", "Asian Tigers", "Globalization",
             "Multi-National Corporations", "The Second Cold War", "The IMF",
             "Solidarity (Poland)", "Margaret Thatcher", "Tiananmen Square",
             "The Revolutions of 1989", "The Gulf War (1991)", "Al Qaeda",
             "The Rwandan Genocide", "The Congo Wars", "Mikhail Gorbachev",
             "Neo-Liberalism", "Structural Adjustment", "The HIV Epidemic",
             "The War on Terror", "The Rise of China", "Climate Change"]

SELECTED_STRINGS = pick_random(QUESTIONS, 15)
LONGEST_STRING = longest_string(SELECTED_STRINGS)
OUTPUT_STRING = format_output(SELECTED_STRINGS, LONGEST_STRING, 3)

print OUTPUT_STRING
