import React from "react";
import { Map, Marker, Popup, TileLayer } from "react-leaflet";
import { Icon } from "leaflet";
import "./local.css";
import * as parkData from "../data/skateboard-parks.json";
import useSWR from "swr";

const fetcher = (...args) => fetch(...args).then((response) => response.json());

export default function RemoteSource() {
  const url =
    "https://data.police.uk/api/crimes-street/all-crime?lat=52.629829&lng=-1.131592&date=2019-10";
  const { data, error } = useSWR(url, { fetcher });
  const crimes = data && !error ? data.slice(0, 100) : [];
  const a = crimes.length;
  const b = 1;
  if (crimes.length == 0) return <div>loading...</div>;
  return (
    <Map center={[52.6376, -1.135171]} zoom={12}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
      />
      {crimes.map((crime) => (
        <Marker
          key={crime.id}
          //   position={[crime.location.latitude, crime.location.longitude]}
          position={[52.6376, -1.135171]}
        />
      ))}
    </Map>
  );
}
