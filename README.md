# Introduction

The dual challenges of mining and deforestation have emerged as critical global concerns, drawing widespread attention from both consumers and companies. These interconnected issues have far-reaching and devastating consequences, including trade restrictions, infrastructure damage from increasingly severe weather events, and widespread crop failures caused by prolonged droughts and shifts in atmospheric convection patterns. Mining, a cornerstone of industrial development, comes with significant environmental costs. The extraction of minerals often leads to habitat destruction, soil erosion, water contamination, and the release of hazardous pollutants into the atmosphere. Additionally, mining activities frequently contribute to greenhouse gas emissions, further exacerbating climate change. The degradation of ecosystems and depletion of natural resources leave lasting scars on the environment, disrupting local biodiversity and jeopardizing the livelihoods of communities dependent on these landscapes. Similarly, deforestation accelerates these impacts by stripping the planet of its natural carbon sinks, further amplifying climate instability. Forest loss also disrupts weather patterns, reduces soil fertility, and undermines water cycles, compounding the damage initiated by mining practices. The cascading effects are evident across economic and social systems worldwide. Trade limitations arise as nations implement stricter environmental regulations to curb unsustainable practices, impacting global supply chains. Extreme weather events, such as floods and droughts, devastate communities, while agricultural systems face increasing challenges from soil degradation and water scarcity.


<img src="https://i.natgeofe.com/n/e5d9c3f1-d1ec-482f-9f21-289380be01ae/greenhouse-gases-reference_4x3.jpg" alt="Greenhouse gases, facts and information"/>

Source:https://nationalgeographic.com/environment/article/greenhouse-gases 



Take the Panama Canal for instance: The Panama Canal is a vital global trade route, offering a safer, shorter alternative to the treacherous Drake Passage, where the convergence of three oceans creates powerful currents and winds. Fed by Lake Gatún, the canal facilitates about 13,870 ship transits annually, generating nearly $5 billion in revenue. Since early 2023, however, a prolonged drought has strained canal operations. In October 2023, rainfall dropped 43% below average, reducing daily ship transits from 32 to 31 by August. This drought is driven by El Niño, which shifts the Pacific jet stream, causing drier conditions. Recent years have seen more extreme weather patterns, intensifying droughts and challenging the canal’s ability to sustain global shipping demands.



<img src="https://s7d2.scene7.com/is/image/TWCNews/drought-dry-cracked-terrain1jpg" alt="How Bad is the Drought in California? Depends on Who You Ask"/>

Source:https://spectrumnews1.com/ca/southern-california/weather/2021/03/05/how-bad-is-the-drought-in-california--depends-on-who-you-ask <br/>



The Panama Canal is one of the busiest waterways in the world and a key player in global trade and shipping. It provides a much safer and shorter route compared to the Drake Passage, known for its treacherous waters. The Drake Passage is where the warm and cold waters of three oceans mix, creating strong currents and winds that aren’t blocked by any landmass. The Panama Canal gets its water mainly from Lake Gatún, an artificial lake that supplies water to its locks. On a typical day, about 38 ships pass through the canal, adding up to around 13,870 ships a year and generating nearly $5 billion in revenue.

However, the canal is facing some big challenges. Since early 2023, Panama and the surrounding regions have been experiencing a prolonged drought, with rainfall in October 2023 dropping 43% below average. This has affected the canal’s operations, cutting the daily number of ships passing through from 32 to 31 on average in August 2023. A major factor behind this drought is El Niño, a weather pattern that shifts the Pacific jet stream. This change pushes the jet stream further south and stretches it eastward, leading to drier conditions in some areas. In recent years, these shifts have been more extreme, and the droughts they cause are getting worse. So, what’s going on in the atmosphere? Convection current shifts are a major player in the changing El Niño conditions.

Deforestation, especially in the Amazon, is adding to the problem. Cutting down trees—sometimes illegally—and burning them to clear land releases a lot of CO2, which traps heat in the atmosphere and contributes to global warming. Locally, the lack of tree cover makes the surface temperature increase because there’s no shade, and the sun’s heat directly hits the surface. This heating strengthens convection currents in the air above the cleared areas, which disrupts local weather patterns. The result? Less rainfall and droughts in nearby regions.


<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRf0BudHOf8vn0PHPIlaw4Y0yIGsSMV687yg3r0wK4aHGbqIuZZ&amp;s" alt="Smog Convection Currents - Science World"/>

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRf0BudHOf8vn0PHPIlaw4Y0yIGsSMV687yg3r0wK4aHGbqIuZZ&amp;s" alt="Smog Convection Currents - Science World"/>

Source:https://scienceworld.ca/resource/smog-convection-currents/


# Mining Detector

#### Detection Accuracy

The Amazon basin encompasses an enormous, complex geography extending over 8.5 million square kilometers. For each quarterly dataset, the neural networks make over 100 million assessments for mining. By constrast, in late 2025, the labeled data we withhold to evaluate model performance consists of around 6400 examples. The metrics we derive from the withheld dataset can only be considered roughly indicative of how the networks will perform in extrapolating to the whole of the territory. At threshold t=0.925, the 2025 model ensemble operates with a precision of 99.6% and a recall of 79.6% for the detection of mine scars, which translates to an overall accuracy of 98.1%. Those metrics apply before post-processing, aggregation of detections to polygons, and human review.

For the 2024 models, which yield the 2018-2023 data on the Amazon Mining Watch website, we ran the following complimentary test. We evaulated by hand a random sample of 500 patch detections from 2023-year data. Of the 500 samples, 498 show scars from artisanal mining. One is an industrial mine, and one is a remnant of the construction of the Balbina dam and power station from around 1985. From this, we can estimate the precision or positive predictive value for that classifier again (in a numerical coincidence) to be 99.6%. In essence, the precision tells you the likelihood that a patch marked as a mine is actually a mine. 

![mining-header-planet](https://user-images.githubusercontent.com/13071901/146877590-b083eace-2084-4945-b739-0f8dda79eaa9.jpg)

#### Area estimation

The mining of concern here touches every country in the Amazon basin. In the typical process, miners slash the rainforest to bare earth and then pump water through underlying sediments to liberate the minerals. The goal of this work is mine detection rather than area estimation, and our classification operates on square image patches covering around twenty hectares each. If the network determines a patch to contain a mine scar, we compute the mined area within the patch by masking and excluding intact vegetation using the Normalized Difference Vegetation Index (NDVI). This yields good masks in forest backgrounds. Area estimates will have higher uncertainties over bare ground and rangelands.

Scars from the mining can be seen from satellite. On the banks of a river, you will observe muddy flats jumbled together with multi-colored toxic wastewater pools. The pools can be brown, tan, yellow, different shades of green, even turquoise. For the most part they are irregular in size, shape, and orientation. Often nearby you can observe miners' encampments, perhaps with blue-tarped tents, and in well-developed mines, a dirt airstrip cut to fly in miners and to fly out the gold. 

On Amazon Mining Watch, detected mines are delineated by the yellow stroke. Here are some characteristic examples of mines:

![MinesEx](https://user-images.githubusercontent.com/11287904/150804841-fabcef8f-4394-46ff-be11-c87ad789ae19.jpg)
(These are mines.)

With limited bootstrap sampling, we extrapolated to run over the whole of the Amazon basin. There are some false detections, and we encourage users to apply discretion in interpreting the findings. Terrain features that can masquerade as mines include sandbars in rivers, braided rivers, farm ponds, and aquaculture ponds, like so:

<!--![NotMinesEx2](https://user-images.githubusercontent.com/11287904/150863564-0b861bef-5cb0-4ea7-bc8e-440b20bece03.jpg)-->
![NotMinesEx](https://user-images.githubusercontent.com/11287904/150816991-7ca7c55f-1c27-460f-bfec-bbdd3e2146ed.jpg)
(These are _not_ mines.)

You can recognize aquaculture ponds by their geometric shape, efficient use of space, and presence in agricultural zones. 

From the March 2024 data release, we note in particular some false positives from aquaculture and other wet industrial operations around Manaus and an area of landslides in hilly terrain of southern Loreto, Peru.

A more common model error is the _false negative_, where the model fails to detect a mine or the full extent of a mine. 

Where the rainforest has begun to heal, mine scars may not be detected in later years, and so mined area both expands and recedes over time. We see some value in this model response and we decided not to correct it. 

On the whole, false detections are relatively few given how widespread the mining is, and we hope this will be a useful resource to those interested in tracking mining activity in the region. 


