DUMMY_DATA = [
    {
        "docno": "alweuj9",
        "title": "Culpa minim deserunt nisi nisi",
        "content": "nisi eu ex minim consectetur dolore et mollit dolore ipsum et consectetur eiusmod commodo nisi ea elit pariatur consequat exercitation et id nostrud deserunt et ad dolor consequat nisi occaecat sed sit ea cupidatat laboris esse occaecat ut et in magna anim excepteur sint ipsum eiusmod anim laboris cillum enim"
    },
    {
        "docno": "2094n5y",
        "title": "Ullamco laboris deserunt ad sit",
        "content": "incididunt occaecat occaecat laboris id irure esse exercitation exercitation anim dolor eiusmod ut lorem ad incididunt dolore tempor reprehenderit reprehenderit qui tempor fugiat in voluptate occaecat cupidatat aliqua incididunt irure proident voluptate aliquip exercitation ipsum in proident esse laboris consequat magna reprehenderit duis do pariatur ut aliqua ad duis magna"
    },
    {
        "docno": "02e8c5h",
        "title": "Ex commodo ipsum aliqua eiusmod",
        "content": "aliqua consequat voluptate sed minim et et enim ut enim consequat ea cupidatat dolore deserunt ex consectetur nostrud sunt labore ut officia dolore consequat ex sunt ea aliquip quis nostrud dolor laborum amet pariatur proident amet deserunt nisi magna exercitation aute ipsum eu ad commodo cillum eu lorem aliquip culpa"
    },
    {
        "docno": "lwa4f98",
        "title": "Pariatur nostrud officia ea consequat",
        "content": "sit cillum culpa proident eiusmod ut irure ut culpa laborum sit dolore ut aliquip incididunt laborum ut in culpa quis non consequat eiusmod dolor reprehenderit irure in aute cupidatat duis et excepteur ut eu eiusmod ullamco proident eu eiusmod tempor tempor reprehenderit veniam laboris in in reprehenderit quis ut do"
    },
    {
        "docno": "oiewv59",
        "title": "Ad deserunt nostrud non in",
        "content": "quis nisi irure proident est eu elit occaecat laboris mollit non ut qui laboris do excepteur ut sunt in reprehenderit tempor voluptate id lorem consectetur do non quis ut dolore consequat lorem ex sunt veniam consectetur id eu adipiscing nulla ex laboris ut sed sed esse do nulla mollit elit"
    }
]
def get_result():
    result = []
    for data in DUMMY_DATA:
        dummy = dict()
        dummy["docno"] = data["docno"]
        dummy["title"] = data["title"]
        dummy["content"] = data["content"][:72] + "..."
        result.append(dummy)
    return result


def get_data_by_docno(docno):
    for data in DUMMY_DATA:
        if data["docno"] == docno:
            return {
                "title": data["title"],
                "content": data["content"]
            }
    else:
        raise ValueError("No document found.")