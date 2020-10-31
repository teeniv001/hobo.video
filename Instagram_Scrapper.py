import csv
import re
import instaloader

#enter instagram login crendentials in place of username and password
L=instaloader.Instaloader()
L.login('rugnedarze@nedoz.com', 'iostream')

#enter the list of accounts for scrapping 
accounts = ['therock','dhanashreevermacompany']

for i in range(len(accounts)):
    pro = accounts[i]
    try:
        #csv 
        print('Getting followers from',pro)
        filename = 'downloads/'+pro+'.csv'
        with open(filename,'a',newline='',encoding="utf-8") as csvf:
            csv_writer = csv.writer(csvf)
            csv_writer.writerow(['user_id','username','fullname','is_verified','is_private','media_count','follower_count','following_count','bio','website','emails','scrape_of'])
            

        profile = instaloader.Profile.from_username(L.context,pro)
        main_followers = profile.followers  

        if main_followers >= 1000:    #filter all account having atleast 1k followers
            for person in profile.get_followers(): 
                try:
                    #details of account
                    user_id = person.userid
                    username = person.username
                    fullname  = person.full_name
                    is_verified = person.is_verified
                    is_private = person.is_private
                    media_count  = person.mediacount
                    follower_count = person.followers
                    following_count = person.followees
                    bio = person.biography
                    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", bio)
                    website = person.external_url

                    with open(filename,'a',newline='') as csvf:
                        csv_writer = csv.writer(csvf)
                        csv_writer.writerow([user_id,username,fullname,is_verified,is_private,media_count,follower_count,following_count,bio,website,emails,pro])

                except Exception as e:
                    print(e)
        else:
            print('account having followers leass than 1k\n\n')

    except:
        print('\nHeading to next account\n')

            
