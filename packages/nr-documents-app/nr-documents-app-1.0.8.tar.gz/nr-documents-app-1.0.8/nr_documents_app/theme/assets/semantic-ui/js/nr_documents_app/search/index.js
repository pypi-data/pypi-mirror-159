// Copyright (c) 2022 CESNET
//
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

import { useLayout, GlobalDataContextProvider } from '@js/oarepo_generated_ui'
import * as React from 'react'
import ReactDOM from 'react-dom'
import 'semantic-ui-css/semantic.min.css'

const testLayout = [
  {
    component: 'divided-row',
    separator: {
      component: 'separator',
      color: 'green',
    },
    items: [
      {
        component: 'raw',
        data: 'Hello',
      },
      {
        component: 'raw',
        data: 'World',
      },
      {
        component: 'raw',
        data: ' ',
      },
      {
        component: 'raw',
        data: 'How are you?',
      },
    ],
  },
]

const searchResultItemData = {
  access_status: 'open',
  rights: ['CC BY-ND'],
  title:
    'V\u011bdy o Zemi a souvisej\u00edc\u00ed environment\u00e1ln\u00ed v\u011bdy',
  resource_type: 'Article',
  defended: '(obhájeno)',
  publication_year: '2020',
  language: 'Czech',
  creators: [
    {
      fullName: 'Doe, John',
      nameType: 'Personal',
      authorityIdentifiers: [
        {
          identifier: '1234abcd',
          scheme: 'orcid',
        },
      ],
      affiliations: ['CESNET'],
    },
  ],
  keywords: [
    'klíčové slovo',
    'předmětové heslo',
    'klíčové slovo',
    'klíčové slovo',
    'klíčové slovo',
  ],
  contributors: [
    {
      fullName: 'Smith, Bob',
      nameType: 'Personal',
      role: 'project leader',
    },
    {
      fullName: 'OARepo',
      nameType: 'Organizational',
    },
  ],
  links: {
    self: '/record/1',
  },
  abstract:
    "If it fits i sits lick the other cats, i heard this rumor where the humans are our owners, pfft, what do they know?!. Lick the curtain just to be annoying. Pet my belly, you know you want to; seize the hand and shred it! found somthing move i bite it tail, it's 3am, time to create some chaos yet somehow manage to catch a bird but have no idea what to do next, so play with it until it dies of shock friends are not food so soft kitty warm kitty little ball of furr meowzer. Eat the fat cats food i want to go outside let me go outside nevermind inside is better so attack the dog then pretend like nothing happened but missing until dinner time, but lick butt and make a weird face so knock dish off table head butt cant eat out of my own dish soft kitty warm kitty little ball of furr. What a cat-ass-trophy! flee in terror at cucumber discovered on floor please let me outside pouty face yay! wait, it's cold out please let me inside pouty face oh, thank you rub against mommy's leg oh it looks so nice out, please let me outside again the neighbor cat was mean to me please let me back inside poop on couch i will be pet i will be pet and then i will hiss. Touch water with paw then recoil in horror sleep on my human's head check cat door for ambush 10 times before coming in give attitude. Gate keepers of hell. Cat sit like bread loved it, hated it, loved it, hated it give attitude, so pee in the shoe. Is good you understand your place in my world sit on human bite nose of your human hiss at vacuum cleaner and car rides are evil so chase little red dot someday it will be mine!. Furball roll roll roll. At four in the morning wake up owner meeeeeeooww scratch at legs and beg for food then cry and yowl until they wake up at two pm jump on window and sleep while observing the bootyful cat next door that u really like but who already has a boyfriend end up making babies with her and let her move in walk on a keyboard and under the bed groom forever, stretch tongue and leave it slightly out, blep yet iâ€™m so hungry iâ€™m so hungry but ew not for that have a lot of grump in yourself because you can't forget to be grumpy and not be like king grumpy cat lick yarn hanging out of own butt. Sleeps on my head lick butt, but human is in bath tub, emergency! drowning! meooowww! and pet right here, no not there, here, no fool, right here that other cat smells funny you should really give me all the treats because i smell the best and omg you finally got the right spot and i love you right now but walk on a keyboard cat jumps and falls onto the couch purrs and wakes up in a new dimension filled with kitty litter meow meow yummy there is a bunch of cats hanging around eating catnip i will be pet i will be pet and then i will hiss. Cat fur is the new black has closed eyes but still sees you and what a cat-ass-trophy! rub my belly hiss and plan steps for world domination gimme attention gimme attention gimme attention gimme attention gimme attention gimme attention just kidding i don't want it anymore meow bye, sleeps on my head. Meowsiers lick human with sandpaper tongue love fish yet small kitty warm kitty little balls of fur drink water out of the faucet. Growl at dogs in my sleep poop in a handbag look delicious and drink the soapy mopping up water then puke giant foamy fur-balls. Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff so you're just gonna scroll by without saying meowdy? meow x. Pushed the mug off the table stand in front of the computer screen, or more napping, more napping all the napping is exhausting plan your travel lie in the sink all day but floof tum, tickle bum, jellybean footies curly toes relentlessly pursues moth. Meow. Somehow manage to catch a bird but have no idea what to do next, so play with it until it dies of shock eat the rubberband so make meme, make cute face sugar, my siamese, stalks me (in a good way), day and night yet find empty spot in cupboard and sleep all day or i will ruin the couch with my claws experiences short bursts of poo-phoria after going to the loo. Ccccccccccccaaaaaaaaaaaaaaatttttttttttttttttssssssssssssssss meowing non stop for food and jump on fridge and thinking about you i'm joking it's food always food, stuff and things for howl uncontrollably for no reason. Woops poop hanging from butt must get rid run run around house drag poop on floor maybe it comes off woops left brown marks on floor human slave clean lick butt now jump on fridge demand to have some of whatever the human is cooking, then sniff the offering and walk away prance along on top of the garden fence, annoy the neighbor's dog and make it bark hiiiiiiiiii feed me now funny little cat chirrup noise shaking upright tail when standing next to you and swipe at owner's legs. Scratch the postman wake up lick paw wake up owner meow meow plop down in the middle where everybody walks. Growl at dogs in my sleep i just saw other cats inside the house and nobody ask me before using my litter box. Chase imaginary bugs ha ha, you're funny i'll kill you last, or i like big cats and i can not lie or if it fits, i sits cat fur is the new black .",
}

const searchResultItem = [
  {
    component: 'grid',
    container: false,
    columnsPerRow: 2,
    columns: [
      {
        className: 'result-item-aside two wide',
        style: {
          alignItems: 'center',
        },
        width: '1',
        items: [
          {
            component: 'icon',
            dataField: 'access_status',
            iconSet: {
              open: {
                src:
                  'https://github.com/Narodni-repozitar/nr-ui/raw/master/public/icons/locks/zamky_open_access.png',
              },
            },
          },
          {
            component: 'icon',
            dataField: 'rights',
            iconSet: {
              'CC BY-ND': {
                src:
                  'https://raw.githubusercontent.com/Narodni-repozitar/nr-ui/master/src/assets/licenses/by-nd.png',
              },
            },
          },
        ],
      },
      {
        items: [
          {
            component: 'header',
            dataField: 'title',
            size: 'large',
          },
          {
            component: 'divided-row',
            separator: {
              component: 'separator',
              double: true,
            },
            items: [
              {
                component: 'list',
                dataField: 'creators',
                horizontal: true,
                separator: {
                  component: 'separator',
                },
                item: {
                  component: 'span',
                },
              },
              {
                component: 'list',
                dataField: 'contributors',
                horizontal: true,
                separator: {
                  component: 'separator',
                },
                item: {
                  component: 'span',
                  className: 'text-gray',
                },
              },
            ],
          },
          {
            component: 'divided-row',
            separator: {
              component: 'separator',
            },
            items: [
              {
                component: 'span',
                dataField: 'publication_year',
              },
              {
                component: 'span',
                dataField: 'language',
              },
            ],
          },
          {
            component: 'row',
            columns: [
              {
                component: 'span',
                dataField: 'resource_type',
              },
              {
                component: 'span',
                dataField: 'defended',
              },
            ],
          },
          {
            component: 'row',
            columns: [
              {
                component: 'list',
                horizontal: true,
                divided: true,
                dataField: 'keywords',
                item: {
                  component: 'link',
                  href: '#',
                },
              },
            ],
          },
          {
            component: 'truncated-text',
            dataField: 'abstract',
            lines: 3,
          },
        ],
      },
    ],
  },
]

const testData = {}

console.log('You know, for documents search!')

const appRoot = document.querySelector('#search-app')

const SearchLayout = ({ layout, data, useGlobalData = false }) =>
  useLayout({ layout, data, useGlobalData })

ReactDOM.render(
  <GlobalDataContextProvider value={searchResultItemData}>
    <SearchLayout layout={searchResultItem} data={searchResultItemData} />
  </GlobalDataContextProvider>,
  appRoot,
)
