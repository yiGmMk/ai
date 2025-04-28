---
title: "What is LiDAR and How Does it Work?"
date: "2024-07-26"
tags: ["LiDAR", "Light Detection and Ranging", "Autonomous Vehicles", "Distance Sensing", "3D Modeling"]
categories: ["Technology", "Engineering"]
description: "LiDAR, or Light Detection and Ranging, is an optical technology used for distance sensing, particularly crucial in autonomous vehicles and various other applications."
author: "Synopsys"
image: ""
---

- LiDAR uses laser light to measure distances.
- It's a key technology for autonomous vehicles.
- It has various applications in remote sensing, atmospheric science, and more.

## Definition

LiDAR is an acronym for Light Detection and Ranging. In LiDAR, laser light is sent from a source (transmitter) and reflected from objects in the scene. The reflected light is detected by the system receiver and the time of flight (TOF) is used to develop a distance map of the objects in the scene.

LiDAR is an optical technology often cited as a key method for distance sensing for [autonomous vehicles](https://www.synopsys.com/automotive/what-is-autonomous-car.html). Many manufacturers are working to develop cost-effective, compact LiDAR systems. Virtually all producers pursuing autonomous driving consider LiDAR a key enabling technology, and some LiDAR systems are already available for [Advanced Driver Assistance Systems (ADAS)](https://www.synopsys.com/automotive/what-is-adas.html).

![Image 12: LiDAR in autonomous cars | Synopsys](https://images.synopsys.com/is/image/synopsys/glossary-osg-lidar-autonomous-cars-street)

_A birds-eye view of the concept of LiDAR systems used in Advanced Driver Assistance Systems._

![Image 13: LiDAR sensor for self-driving car | Synopsys](https://images.synopsys.com/is/image/synopsys/glossary-osg-lidar-side-mirror-sensor)

_LiDAR sensor for self-driving car, located under a side mirror. LiDAR systems can also be located on top of an autonomous car._

***

## How Does LiDAR Work and How Does It Provide Solutions?

Essentially, LiDAR is a ranging device, which measures the distance to a target. The distance is measured by sending a short laser pulse and recording the time lapse between outgoing light pulse and the detection of the reflected (back-scattered) light pulse.

![Image 14: LiDAR is a ranging device, which measures the distance to a target | Synopsys](https://images.synopsys.com/is/image/synopsys/lidar-glossary)

Click to see the detail

×

![Image 15: LiDAR is a ranging device, which measures the distance to a target | Synopsys](https://images.synopsys.com/is/image/synopsys/lidar-glossary)

A LiDAR system may use a scan mirror, multiple laser beams, or other means to "scan" the object space. With the ability to provide accurate measurement of distances, LiDAR can be used to solve many different problems.

In remote sensing, LiDAR systems are used to measure scatter, absorption, or re-emission from particles or molecules in the atmosphere. For these purposes, the systems may have specific requirements on the wavelength of the laser beams.  The concentration of a specific molecular species in the atmosphere, e.g. methane and the aerosol loading, can be measured. Rain droplets in the atmosphere can be measured to estimate the distance of a storm and the rain fall rate.

Other LiDAR systems provide profiles of three-dimensional surfaces in the object space. In these systems, the probing laser beams are not tied to specific spectral features. Instead, the wavelength of the laser beams may be chosen to ensure eye safety or to avoid atmospheric spectral features. The probing beam encounters and is reflected by a "hard target" back to the LiDAR receiver.

LiDAR can also be used to determine the velocity of a target. This can be done either through the Doppler technique or measuring the distance to a target in rapid succession. For example, atmospheric wind velocity and the velocity of an automobile can be measured by a LiDAR system.

In addition, LiDAR systems can be used to create a three-dimensional model of a dynamic scene, such as what may be encountered by an autonomous driving vehicle. This can be done in various ways, usually using a scanning technique.

***

## What Are the Challenges With LiDAR?

Essentially, LiDAR is a ranging device, which measures the distance to a target. The distance is measured by sending a short laser pulse and recording the time lapse between outgoing light pulse and the detection of the reflected (back-scattered) light pulse.

There are some well-known challenges with operational LiDAR systems. These challenges depend on the type of LiDAR system. Here are some examples:

*   The isolation and rejection of signal from the emitted beam - The radiance of the probing beam is generally much greater than that of the return beam. Care must be taken to make sure the probing beam is not reflected or scattered by the system back into the receiver such that the detector is saturated and unable to detect external targets.
    
*   Spurious returns from debris in the atmosphere between the transmitter and the intended targets - The debris can cause such a strong spurious return that the return from the intended targets is not reliably detected.
    
*   Limitations on available optical power -A system with more power in the beam provides higher accuracy but is more expensive to operate.
    
*   Scanning speed-Safety can be an issue when the laser source is operating at a frequency dangerous to human eyes.  This issue is being mitigated by other approaches such as flash LiDAR which illuminate a large area all at once and by operating at eye-safe wavelengths.
    
*   Device crosstalk-signals from nearby LiDAR devices might interfere with the signal of interest.  The challenge faced now is how to differentiate signals emitted by other LiDAR devices nearby.   Various approaches with signal chirping and isolation are under development.
    
*   Cost and maintenance of LiDAR systems – These systems are more expensive than some alternative types of sensors however there is active development to overcome the high cost and produce systems at lower prices for wider use.  Rejection of returns from unintended objects- This is similar to the rejection of atmospheric spurious signal as mentioned previously. However, it can also happen in clear air scenarios. Addressing this challenge generally involves minimizing the size of the beam at various target distances as well as over the field-of-view received back at the LiDAR receiver.
    

***

## What Other Applications Are There for LiDAR?

The application areas for LiDAR are deep and varied.  In atmospheric sciences, LiDAR has been used for the detection of many types of atmospheric constituents. It has been used to characterize aerosols in the atmosphere, investigate upper atmospheric winds, profile clouds, aid the collection of weather data, and many other applications. In astronomy, LiDAR has been used to measure distances, both for distant objects such as the moon and for very near objects. In fact, LiDAR is a crucial device for improving the measurement of the distance to the moon up to millimeter precision. LIDAR has also been used to create guide stars for astronomy applications.

![Image 16: Leosphere Windcube Scanning LiDAR measures wind for development and operations applications - NOAA | Synopsys](https://images.synopsys.com/is/image/synopsys/glossary-osg-lidar-leosphere-windcube)

_Automobile sensors in self-driving cars use camera data, radar, and LiDAR to detect objects around it.  
Source: NOAA and [https://lidarmag.com/2019/12/04/not-just-for-surveying-lidars-big-impact-in-weather/](https://lidarmag.com/2019/12/04/not-just-for-surveying-lidars-big-impact-in-weather/)_

![Image 17: LiDAR data on the Bixby Bridge in Big Sur, California - NOAA | Synopsys](https://images.synopsys.com/is/image/synopsys/glossary-osg-lidar-noaa-big-sur)

_LiDAR data is often collected by air, such as with this NOAA survey aircraft (right) over Bixby Bridge in Big Sur, Calif. Here, LiDAR data revelas a top-down (top left) and profile view of Bixby Bridge. NOAA scientists use LiDAR-generated products to examine both natural and manmade environments. LiDAR data supports activities such as inundation and storm surge modeling, hydrodynamic modeling, shoreline mapping, emergency response, hydropgraphic surveying, and coast vulnerability analysis._

_Source: NOAA - [https://geodesy.noaa.gov/INFO/facts/lidar.shtml](https://geodesy.noaa.gov/INFO/facts/lidar.shtml)_

Furthermore, topographic LiDAR uses a near-infrared laser to map the land and buildings, and bathymetric LiDAR uses water-penetrating green light to map seafloor and riverbed. In agriculture, LiDAR can be used to map topology and crop growth, which can provide information on fertilizer needs and irrigation requirements. In archaeology, LiDAR has been used to map ancient transportation systems under thick forest canopy.

Today, LiDAR is frequently used to create a three-dimensional model of the world around the LiDAR sensor. Autonomous navigation is one application that uses the point cloud created by a LiDAR system. Miniature LiDAR systems can even be found in devices as small as mobile phones.

***

## How Does LiDAR Play Out in a Real-World Situation?

One fascinating application for LiDAR is situational awareness for things like autonomous navigation. The situational awareness system for any moving vehicle needs to be aware of both stationary and moving objects around it. For example, radar has been used for a long time in detecting aircraft. LiDAR has been found very helpful for terrestrial vehicles because it can ascertain the distance to objects and is very precise in terms of directionality. The probing beams can be directed to precise angles and scanned quickly to create the point cloud for the three-dimensional model. The ability to scan quickly is key for this application since the situation surrounding the vehicle is highly dynamic.

![Image 18: Autonomous sensors in self-driving cars | Synopsys](https://images.synopsys.com/is/image/synopsys/glossary-osg-lidar-autonomous-car-functions)

Click to see the detail

×

![Image 19: Autonomous sensors in self-driving cars | Synopsys](https://images.synopsys.com/is/image/synopsys/glossary-osg-lidar-autonomous-car-functions)

_Automobile sensors in self-driving cars use camera data, radar, and LiDAR to detect objects around it_

![Image 20: Autonomous car uses LiDAR sensors to detect surrounding buildings and cars | Synopsys](https://images.synopsys.com/is/image/synopsys/glossary-osg-lidar-vehicle-sensing-buildings)

_Autonomous car uses LiDAR sensors to detect surrounding buildings and cars_

***

## What Software Is Needed for LiDAR Devices?

Software is key to every aspect of LiDAR system creation and operation. There are multiple software needs for the design of LiDAR systems. The system engineer needs a radiometric model to predict the signal-to-noise ratio of the return beam. The optical engineer needs software to create the optical design. The electronics engineer needs an electronics model to create the electrical design. The mechanical engineer needs a CAD package to accomplish the system layout. Structural and thermal modeling software may also be needed. The operation of LiDAR systems requires control software and reconstruction software that converts the point cloud to a three-dimensional model.

Synopsys offers several optical and photonic tools to support LiDAR system and components design:

*   [**CODE V**](https://www.synopsys.com/optical-solutions/codev.html) optical design software for designing receiver optics in a LiDAR system
    *   Refer to: [Application in Optical Design: Optimization for Receiver Enclosed Energy in LiDAR Systems](https://www.synopsys.com/content/dam/synopsys/optical-solutions/documents/whitepapers/code-v-lidar-enclosed-energy-systems-wp.pdf)

![Image 21: CODE V optical design software for LiDAR systems | Synopsys](https://images.synopsys.com/is/image/synopsys/osg-glossary-code-v-lidar)

_Optimized LiDAR receiver optical system, simulated in CODE V_

[Learn More About CODE V](https://www.synopsys.com/optical-solutions/codev.html)

*   [**LightTools**](https://www.synopsys.com/optical-solutions/lighttools.html) illumination design software for modeling and analyzing LiDAR systems 
    *   Read more: [Capabilities for LiDAR and Laser Sources](https://www.synopsys.com/optical-solutions/e-news/lighttools/2020-december.html)

![Image 22: LiDAR optical system, simulated in LightTools | Synopsys](https://images.synopsys.com/is/image/synopsys/glossary-osg-ray-tracing-lighttools-lidar2)

_LiDAR optical system, simulated in LightTools_

[Learn More About LightTools](https://www.synopsys.com/optical-solutions/lighttools.html)

*   [**Photonic Solutions**](https://www.synopsys.com/photonic-solutions.html) simulation tools can be used for optimizing the design of various components. 
    *   [RSoft tools](https://www.synopsys.com/photonic-solutions/rsoft-photonic-device-tools.html) can support the complicated design layout of an [on-chip LiDAR device](https://www.synopsys.com/photonic-solutions/product-applications/lidar/lidar-on-chip.html). No single simulation tool can solve the complex problem of a design of this nature. Combining RSoft tools such as [FullWAVE FDTD](https://www.synopsys.com/photonic-solutions/rsoft-photonic-device-tools/passive-device-fullwave.html) for the Emitter, [Multiphysics Utility](https://www.synopsys.com/photonic-solutions/rsoft-photonic-device-tools/multiphysics-utility.html) for the T-O Phaser, and [BeamPROP BPM](https://www.synopsys.com/photonic-solutions/rsoft-photonic-device-tools/passive-device-beamprop.html) for the splitter will achieve the optimal layout. 
        
    *   [OptSim](https://www.synopsys.com/photonic-solutions/optsim/single-mode-network.html) for the design and simulation of optical communication systems
        
        *   [Time-of-flight (ToF) Resolution and Measurement from Received RF Spectra in Optical Coherence Tomography (OCT) and Light Detection and Ranging (LiDAR) Applications](https://www.synopsys.com/photonic-solutions/product-applications/tof-lidar.html)
        
    *   [OptoCompiler](https://www.synopsys.com/photonic-solutions/optocompiler.html) for photonic integrated circuit design
        
        *   The application area for the photonic integrated circuits is also becoming much wider ranging from data center interests such as transceivers and switches to more diverse automotive, biomedical and sensing markets such as (solid-state) LiDAR, tomography and free-space sensors.

![Image 23: RSoft Photonic Device Tools for LiDAR simulation | Synopsys](https://images.synopsys.com/is/image/synopsys/osg-glossary-rsoft-tools-lidar-on-chip)

_Combined RSoft tools used for different elements of the  
LiDAR-On-Chip design_

[Learn More about Photonic Solutions](https://www.synopsys.com/photonic-solutions.html)
