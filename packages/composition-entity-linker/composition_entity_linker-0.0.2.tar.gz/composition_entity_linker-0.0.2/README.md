# Composition Entity Linker (under development)

This is a tool for linking classical music record & track to the corresponding composition / movement. The reference corpus is based on databased crawled from https://imslp.org/wiki/Main_Page.


### install 
```pip install composition-entity-linker```

### usage 
```
from composition_entity_linker import CELlinker, Track
linker = CELlinker()
```

#### query the composition from track name:
```
track = Track("Violin Sonata in A Major, Op. 162, D. 574 ""Grand Duo"": III. Andantino (Live)", composer="Franz Schubert")
composition = linker.query(track)
```

#### compare if the two tracks are refering to the same composition: 
```
track1 = Track("Prelude and Fugue No. 2 in C Minor BWV 847")
track2 = Track("Prelude & Fugue In C Minor (Well-Tempered Clavier, Book I, No. 2), BWV 847")
linker.compare(track1, track2)
```

### Track info
```
Track(title: str, 
    duration: float in ms,
    composer: str)
```

