moanalocations= {
               'Hidden Cavern': {
                        'north' : 'Mauis Cave',
                        'east' :  'Family Hut',
                        'item' :  'sail boat',
                        },
               'Family Hut' : {
                        'west' : 'Hidden Cavern', 
                        'item' : 'pendant',
                        },
               'Mauis Cave' : {
                       'north' : 'Cave of Monsters',
                       'south' : 'Hidden Cavern',
                       'item' : 'Chicken named Hei He has no real value but great company',
                       },
               'Cave of Monsters' : {
                       'south' : 'Mauis Cave',
                       'north' : 'Tefiti mountain',
                       'item' : 'Mauis hook',
                       },
               'Tefiti mountain': {
                       'south' : 'Cave of Monsters',
                       'return' : 'Heart of Tefiti',
                       }, 
                }
threelittlepigslocation= {
               'Moma Pig': {
                        'south' : 'Woods',
                          },
               'Woods': {
                        'north' : 'Moma Pig', 
                        'item' : 'straw',
                        'south': 'Sticks'
                        },
                'Sticks' : {
                         'south' : 'Bricks',
                         'north' : 'Woods',
                          'item' : 'sticks'
                   },
                          'Bricks' : {
                          'southeast': 'Little Pig 1',
                          'north' : 'Sticks',
                          'southwest':'Little Pig 2',
                           'west' : 'Little Pig 3'
                   },
             
               'Little Pig 1' : {
                       'southeast' : 'straw',
                       'southwest' : 'Little Pig 2',
                       'north' :     'Sticks',
                       'west' :      'Bricks',
                       },
               'Little Pig 2': {
                       'southwest' : 'sticks',
                       'southeast' : 'Little Pig 1',
                       'west' :      'Little Pig 3',
                       },   
               'Little Pig 3' : {
                        'west':  'Little Pig 3',
                        'southwest' : 'Little Pig 2'
                        'north' :   ' Bricks'
                       },
              'Big Bad Wolf: {
                      'southeast':  'Runs to the house of straw huffs and puffs and blows the house down',
                      'southwest':  'Runs to the house of sticks huffs and puffs and blows the house down',
                      'north':  'Runs to the house of bricks and huffs and puffs with no success',
                      'up' : 'Climbs on top of the roof to enter the chimney and gets burned in boiling water and shoots out to the sky'
                      }
  
  
