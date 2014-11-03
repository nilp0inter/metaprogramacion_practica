ENDPOINTS = {'TrelloV1': {'actions': {'METHODS': ['GET', 'GET', 'DELETE'],
                          'board': {'METHODS': ['GET', 'GET']},
                          'card': {'METHODS': ['GET', 'GET']},
                          'entities': {'METHODS': ['GET']},
                          'list': {'METHODS': ['GET', 'GET']},
                          'member': {'METHODS': ['GET', 'GET']},
                          'memberCreator': {'METHODS': ['GET', 'GET']},
                          'organization': {'METHODS': ['GET', 'GET']}},
              'batch': {'METHODS': ['GET']},
              'boards': {'METHODS': ['GET', 'GET', 'POST'],
                         'actions': {'METHODS': ['GET']},
                         'boardStars': {'METHODS': ['GET']},
                         'calendarKey': {'generate': {'METHODS': ['POST']}},
                         'cards': {'METHODS': ['GET', 'GET', 'GET']},
                         'checklists': {'METHODS': ['GET', 'POST']},
                         'deltas': {'METHODS': ['GET']},
                         'emailKey': {'generate': {'METHODS': ['POST']}},
                         'lists': {'METHODS': ['GET', 'GET', 'POST']},
                         'markAsViewed': {'METHODS': ['POST']},
                         'members': {'METHODS': ['GET', 'GET', 'DELETE'],
                                     'cards': {'METHODS': ['GET']}},
                         'membersInvited': {'METHODS': ['GET', 'GET']},
                         'memberships': {'METHODS': ['GET', 'GET']},
                         'myPrefs': {'METHODS': ['GET']},
                         'organization': {'METHODS': ['GET', 'GET']},
                         'powerUps': {'METHODS': ['POST', 'DELETE']}},
              'cards': {'METHODS': ['GET', 'GET', 'POST', 'DELETE'],
                        'actions': {'METHODS': ['GET'],
                                    'comments': {'METHODS': ['POST',
                                                             'DELETE']}},
                        'attachments': {'METHODS': ['GET', 'GET', 'POST',
                                                    'DELETE']},
                        'board': {'METHODS': ['GET', 'GET']},
                        'checkItemStates': {'METHODS': ['GET']},
                        'checklist': {'checkItem': {'METHODS': ['POST',
                                                                'DELETE'],
                                                    'convertToCard': {'METHODS': ['POST']}}},
                        'checklists': {'METHODS': ['GET', 'POST', 'DELETE']},
                        'idMembers': {'METHODS': ['POST', 'DELETE']},
                        'labels': {'METHODS': ['POST', 'DELETE']},
                        'list': {'METHODS': ['GET', 'GET']},
                        'markAssociatedNotificationsRead': {'METHODS': ['POST']},
                        'members': {'METHODS': ['GET']},
                        'membersVoted': {'METHODS': ['GET', 'POST',
                                                     'DELETE']},
                        'stickers': {'METHODS': ['GET', 'GET', 'POST',
                                                 'DELETE']}},
              'checklists': {'METHODS': ['GET', 'GET', 'POST', 'DELETE'],
                             'board': {'METHODS': ['GET', 'GET']},
                             'cards': {'METHODS': ['GET', 'GET']},
                             'checkItems': {'METHODS': ['GET', 'GET',
                                                        'POST', 'DELETE']}},
              'lists': {'METHODS': ['GET', 'GET', 'POST'],
                        'actions': {'METHODS': ['GET']},
                        'archiveAllCards': {'METHODS': ['POST']},
                        'board': {'METHODS': ['GET', 'GET']},
                        'cards': {'METHODS': ['GET', 'GET', 'POST']},
                        'moveAllCards': {'METHODS': ['POST']}},
              'members': {'METHODS': ['GET', 'GET'],
                          'actions': {'METHODS': ['GET']},
                          'avatar': {'METHODS': ['POST']},
                          'boardBackgrounds': {'METHODS': ['GET', 'GET',
                                                           'POST', 'DELETE']},
                          'boardStars': {'METHODS': ['GET', 'GET', 'POST',
                                                     'DELETE']},
                          'boards': {'METHODS': ['GET', 'GET']},
                          'boardsInvited': {'METHODS': ['GET', 'GET']},
                          'cards': {'METHODS': ['GET', 'GET']},
                          'customBoardBackgrounds': {'METHODS': ['GET',
                                                                 'GET',
                                                                 'POST',
                                                                 'DELETE']},
                          'customEmoji': {'METHODS': ['GET', 'GET', 'POST']},
                          'customStickers': {'METHODS': ['GET', 'GET',
                                                         'POST', 'DELETE']},
                          'deltas': {'METHODS': ['GET']},
                          'idBoardsPinned': {'METHODS': ['POST', 'DELETE']},
                          'notifications': {'METHODS': ['GET', 'GET']},
                          'oneTimeMessagesDismissed': {'METHODS': ['POST']},
                          'organizations': {'METHODS': ['GET', 'GET']},
                          'organizationsInvited': {'METHODS': ['GET', 'GET']},
                          'savedSearches': {'METHODS': ['GET', 'GET',
                                                        'POST', 'DELETE']},
                          'tokens': {'METHODS': ['GET']},
                          'unpaidAccount': {'METHODS': ['POST']}},
              'notifications': {'METHODS': ['GET', 'GET'],
                                'all': {'read': {'METHODS': ['POST']}},
                                'board': {'METHODS': ['GET', 'GET']},
                                'card': {'METHODS': ['GET', 'GET']},
                                'entities': {'METHODS': ['GET']},
                                'list': {'METHODS': ['GET', 'GET']},
                                'member': {'METHODS': ['GET', 'GET']},
                                'memberCreator': {'METHODS': ['GET', 'GET']},
                                'organization': {'METHODS': ['GET', 'GET']}},
              'organizations': {'METHODS': ['GET', 'GET', 'POST', 'DELETE'],
                                'actions': {'METHODS': ['GET']},
                                'boards': {'METHODS': ['GET', 'GET']},
                                'deltas': {'METHODS': ['GET']},
                                'logo': {'METHODS': ['POST', 'DELETE']},
                                'members': {'METHODS': ['GET', 'GET',
                                                        'DELETE'],
                                            'all': {'METHODS': ['DELETE']},
                                            'cards': {'METHODS': ['GET']}},
                                'membersInvited': {'METHODS': ['GET', 'GET']},
                                'memberships': {'METHODS': ['GET', 'GET']},
                                'prefs': {'associatedDomain': {'METHODS': ['DELETE']},
                                          'orgInviteRestrict': {'METHODS': ['DELETE']}},
                                'unpaidAccount': {'METHODS': ['POST']}},
              'search': {'METHODS': ['GET'], 'members': {'METHODS': ['GET']}},
              'sessions': {'METHODS': ['POST'],
                           'socket': {'METHODS': ['GET']}},
              'tokens': {'METHODS': ['GET', 'GET', 'DELETE'],
                         'member': {'METHODS': ['GET', 'GET']},
                         'webhooks': {'METHODS': ['GET', 'GET', 'POST',
                                                  'DELETE']}},
              'types': {'METHODS': ['GET']},
              'webhooks': {'METHODS': ['GET', 'GET', 'POST', 'DELETE']}}}