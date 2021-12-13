import React from "react";
import * as L from "leaflet";

import {
  MapContainer,
  Marker,
  Popup,
  TileLayer,
  Polyline,
  Polygon,
  Circle,
  Tooltip,
} from "react-leaflet";
import "./local.css";
import useSWR from "swr";

const fetcher = (...args) => fetch(...args).then((response) => response.json());

export default function RemoteSource() {
  const purpleOptions = { fillcolor: "red", color: "lime" };
  const redOptions = { fillcolor: "red", color: "lime" };

  const url =
    "https://data.police.uk/api/crimes-street/all-crime?lat=52.629829&lng=-1.131592&date=2019-10";
  const { data, error } = useSWR(url, { fetcher });
  const crimes = data && !error ? data.slice(0, 10) : [];

  const positions3 = [];
  crimes.map((crime) =>
    positions3.push([crime.location.latitude, crime.location.longitude])
  );
  const positions = positions3.slice(1, 4);
  const positions2 = positions3.slice(5, 9);
  //   return <div>{positions}</div>;

  //   const positions2 = [];
  //   crimes.map((crime) =>
  //     positions.push([crime.location.latitude, crime.location.longitude])
  //   );

  return (
    <MapContainer center={[52.6376, -1.135171]} zoom={12}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
      />
      {crimes.map((crime) => (
        <Marker
          key={crime.id}
          //   position={[crime.location.latitude, crime.location.longitude]}
          position={[crime.location.latitude, crime.location.longitude]}
        />
      ))}
      <Polyline pathOptions={purpleOptions} positions={positions} />;
      <Polyline color="red" weight="10" positions={positions2}>
        <Tooltip permanent>sticky Tooltip for Polygon</Tooltip>
      </Polyline>
      <Polyline color="green" weight="5" positions={positions2}></Polyline>
    </MapContainer>
  );
}
